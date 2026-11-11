# V7RC_Blockly_Examples

[繁體中文](README.md) · [简体中文](README.zh-CN.md) · [English](README.en.md) · [日本語](README.ja.md)

本仓库收录 V7RC Blockly 编程示例。

## 示例

- [`blockly_translation.xml`](blockly_translation.xml) · 使用手机麦克风进行中译英并显示结果
- [`blockly-llm-louis-2025-02-10.xml`](blockly-llm-louis-2025-02-10.xml) · 聊天机器人原型
- [`blockly_AI-mqtt.xml`](blockly_AI-mqtt.xml) · 集成 AI 与 MQTT
- [`blockly_GPS_sample.xml`](blockly_GPS_sample.xml) · 读取手机 GPS
- [`blockly_Gyro.xml`](blockly_Gyro.xml) · 读取手机陀螺仪
- [`blockly_v7rc_lego_racing.xml`](blockly_v7rc_lego_racing.xml) · 控制 Legi 系列车辆
- [`blockly_robot_control.xml`](blockly_robot_control.xml) · 控制益成老师的机器人
- [`camera-object-detection/README.md`](camera-object-detection/README.md) · 相机物体检测，显示物体框、名称和保留一位小数的置信度百分比
- [`voice-chatbot/README.md`](voice-chatbot/README.md) · 语音对话 v3／Canvas v4，逐句朗读，播放完毕后恢复录音，Canvas v4 在画布上显示并清除字幕

## 使用 Codex 生成 Blockly XML

```sh
git clone https://github.com/v7rc/V7RC_Blockly_Examples.git
cd V7RC_Blockly_Examples
```

在 Codex 中打开克隆后的仓库，或在仓库目录启动 Codex CLI。调用项目内的 Skill 时输入 `$v7rc-blockly-xml`

```text
$v7rc-blockly-xml 生成 canvas-hello.xml，清除画布图层 0，再在 (30, 50) 绘制黄色文字 Hello V7RC。
```

在编辑器中导入 XML。画布示例请在支持绘图的 V7RC App 中运行。 [编辑器](https://blocky.v7rc.io/)

[开发者文档](https://blocky.v7rc.io/docs/) · [积木目录](https://blocky.v7rc.io/docs/block-catalog.json) · [Skill 目录](.agents/skills/v7rc-blockly-xml/)

## 上传到指定设备

```text
$v7rc-blockly-xml 请上传已验证的 XML。Device ID 为 <你的 Device ID>。
```

也可提供包含 id 的完整编辑器网址。Skill 会备份现有工作区，并在上传后读回比对。请勿公开分享 Device ID。
