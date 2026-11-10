# Upload a workspace by Device ID

Use this workflow when the user requests upload and supplies the target Device ID. This saves the device's server-side Blockly workspace. A later open or reload in the editor or App may be needed to load it.

1. Accept a hyphenated UUID or take the single `id` query value from an HTTPS URL on `blocky.v7rc.io`. The `isvip=1` parameter only controls the editor UI. Treat the ID as sensitive because the deployed editor also uses it as the API token. Keep it out of examples, committed files, and normal logs.
2. Validate the finished XML with the target editor first. If an older online editor drops a native-only field, preserve the validated XML when uploading. Explain any required App version to the user.
3. Run the helper with the XML and target. Use the local dry run first if validation is uncertain, then use `--apply` when the upload is authorized.

   ```sh
   python3 scripts/upload_workspace.py completed.xml --device-id '<DEVICE_ID>' --apply --backup-dir /private/tmp/v7rc-workspace-backups
   ```

4. Report success only after the helper confirms server read-back. Give the backup path if a previous workspace was saved. The helper performs read-back even when the write response is ambiguous. If read-back fails, check the server before any repeat write. If using the editor UI as a fallback, distinguish the upload indicator from verified server read-back.

The public editor bundle checked on 2026-11-10 uses `POST https://blocky-api.v7rc.io/v1/blocky` for both operations. Its `GET` action sends the ID in the token and device headers and in the JSON device field. Its `POST` action sends the ID in the token header and sends the XML string as JSON data. The helper mirrors these operations, backs up a populated workspace before replacing it, and checks the result without running the Blockly program.
