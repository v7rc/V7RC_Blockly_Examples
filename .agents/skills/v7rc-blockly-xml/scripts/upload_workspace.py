#!/usr/bin/env python3
"""Upload a validated Blockly XML workspace to one V7RC device."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import urllib.request
import uuid
import xml.etree.ElementTree as ET

URL = "https://blocky-api.v7rc.io/v1/blocky"
ROOT = "{https://developers.google.com/blockly/xml}xml"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def workspace(xml):
    if "<!doctype" in xml.lower() or "<!entity" in xml.lower():
        raise ValueError("Workspace XML must not contain a DTD or entity declarations.")
    root = ET.fromstring(xml)
    if root.tag != ROOT:
        raise ValueError("Expected a Blockly workspace with the Blockly XML namespace.")
    # Ignore pretty-print indentation while preserving field and comment text.
    for node in root.iter():
        if len(node) and not (node.text or "").strip():
            node.text = None
        if not (node.tail or "").strip():
            node.tail = None
    return ET.canonicalize(ET.tostring(root, encoding="unicode"))


def request(device, action, xml=None):
    headers = {"Content-Type": "application/json", "token": device}
    payload = {"action": action, "device": device}
    if action == "GET":
        headers["device"] = device
    else:
        payload["data"] = xml
    req = urllib.request.Request(URL, json.dumps(payload).encode(), headers, method="POST")
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=15) as response:
        if response.status != 200:
            raise ValueError(f"Unexpected HTTP status {response.status}.")
        result = json.load(response)
        if isinstance(result, str):
            result = json.loads(result)
    if not isinstance(result, dict) or type(result.get("status")) is not int or result["status"] != 0:
        raise ValueError(f"Server did not confirm the {action} operation.")
    return result


def read(device):
    result = request(device, "GET")
    if result.get("errorCode") != "0000" or "data" not in result:
        raise ValueError("Server did not confirm the current workspace.")
    value = result["data"]
    if value is not None and not isinstance(value, str):
        raise ValueError("Unexpected workspace format from the server.")
    return value


def backup(xml, directory):
    directory.mkdir(parents=True, exist_ok=True)
    fd, path = tempfile.mkstemp(prefix="v7rc-workspace-", suffix=".xml", dir=directory)
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as file:
        file.write(xml)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml", type=Path)
    parser.add_argument("--device-id", required=True)
    parser.add_argument("--apply", action="store_true", help="Save to the specified device.")
    parser.add_argument("--backup-dir", type=Path, default=Path.cwd() / "v7rc-workspace-backups")
    args = parser.parse_args()
    attempted = False
    try:
        device = args.device_id.strip()
        if str(uuid.UUID(device)) != device.lower():
            raise ValueError("Use the hyphenated Device ID from the editor URL.")
        xml = args.xml.read_bytes().decode("utf-8-sig")
        expected = workspace(xml)
        digest = hashlib.sha256(xml.encode()).hexdigest()
        if not args.apply:
            print(f"Validated XML (dry run, no request). SHA-256: {digest}")
            return 0
        previous = read(device)
        if previous:
            if workspace(previous) == expected:
                print("The requested workspace is already stored. No upload needed.")
                return 0
            print(f"Previous workspace backup: {backup(previous, args.backup_dir)}", flush=True)
        attempted = True
        write_error = None
        try:
            request(device, "POST", xml)
        except (OSError, ValueError) as error:
            write_error = error
        # The service may save successfully without a status field in the POST reply.
        stored = read(device)
        if not stored or workspace(stored) != expected:
            if write_error:
                raise write_error
            raise ValueError("The workspace read back does not match the XML submitted.")
        print(f"Uploaded and verified by read-back. SHA-256: {digest}")
        return 0
    except (OSError, ValueError, ET.ParseError) as error:
        if attempted:
            parser.exit(1, f"Upload could not be verified: {error} Check the server before retrying.\n")
        parser.exit(1, f"No upload attempted: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
