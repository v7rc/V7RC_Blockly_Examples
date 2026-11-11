# V7RC_Blockly_Examples

[繁體中文](README.md) · [简体中文](README.zh-CN.md) · [English](README.en.md) · [日本語](README.ja.md)

This repository contains programming examples for V7RC Blockly.

## Examples

- [`blockly_translation.xml`](blockly_translation.xml) · Translate spoken Chinese into English and display the result
- [`blockly-llm-louis-2025-02-10.xml`](blockly-llm-louis-2025-02-10.xml) · Chatbot prototype
- [`blockly_AI-mqtt.xml`](blockly_AI-mqtt.xml) · Integrate AI with MQTT
- [`blockly_GPS_sample.xml`](blockly_GPS_sample.xml) · Read the phone’s GPS
- [`blockly_Gyro.xml`](blockly_Gyro.xml) · Read the phone’s gyroscope
- [`blockly_v7rc_lego_racing.xml`](blockly_v7rc_lego_racing.xml) · Control Legi series vehicles
- [`blockly_robot_control.xml`](blockly_robot_control.xml) · Control Teacher Yi-Cheng’s robot
- [`camera-object-detection/README.md`](camera-object-detection/README.md) · Camera object detection with bounding boxes, labels and confidence percentages to one decimal place
- [`voice-chatbot/README.md`](voice-chatbot/README.md) · Voice chat v3 and Canvas v4 with sentence-by-sentence speech and automatic microphone resumption. Canvas v4 draws and clears subtitles on the canvas

## Generate Blockly XML with Codex

```sh
git clone https://github.com/v7rc/V7RC_Blockly_Examples.git
cd V7RC_Blockly_Examples
```

Open the cloned repository as a project in Codex, or start Codex CLI in the repository directory. Invoke the project skill with `$v7rc-blockly-xml`

```text
$v7rc-blockly-xml Generate canvas-hello.xml. Clear canvas layer 0 and draw Hello V7RC in yellow at (30, 50).
```

Import the XML into the editor. Run the canvas example in a V7RC app that supports drawing. [Editor](https://blocky.v7rc.io/)

[Developer docs](https://blocky.v7rc.io/docs/) · [Block catalog](https://blocky.v7rc.io/docs/block-catalog.json) · [Skill directory](.agents/skills/v7rc-blockly-xml/)

## Upload to a device

```text
$v7rc-blockly-xml Upload the validated XML to Device ID <your Device ID>.
```

You can also provide the full editor URL containing the id. The skill backs up the existing workspace and verifies the upload by reading it back. Keep your Device ID private.
