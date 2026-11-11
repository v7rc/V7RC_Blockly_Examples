# V7RC_Blockly_Examples

[繁體中文](README.md) · [简体中文](README.zh-CN.md) · [English](README.en.md) · [日本語](README.ja.md)

這個Repository主要存放V7RC Blocky程式設計的功能範例，提供給V7RC的愛好者參考。

1. blockly_translation.xml: 使用手機的麥克風去進行中翻英，顯示在畫面。

2. blockly-llm-louis-2025-02-10.xml： 交談機器人的雛形

3. blockly_AI-mqtt.xml： AI與MQTT的整合

4. blockly_GPS_sample.xml： 使用手機GPS的範例

5. blockly_Gyro.xml： 使用手機的陀螺儀數據

7. blockly_v7rc_lego_racing.xml： V7RC可以控制Legi科技系列車輛。

8. blockly_robot_control.xml: 使用V7RC控制益成老師的機器人。

9. [相機物件偵測](camera-object-detection/README.md)：使用 iOS V7RC App 的相機畫出物件框、名稱及一位小數的信心度百分比。內含正式 XML 與兩份診斷範例。

10. [語音對話 v3／Canvas v4](voice-chatbot/README.md)：逐句朗讀，播完自動恢復收音。Canvas v4 將字幕繪製在畫布上並在朗讀結束後清除。

## 使用 Codex 生成 V7RC Blockly XML

`v7rc-blockly-xml` Skill 會查閱 [V7RC Blockly 開發者文件](https://blocky.v7rc.io/docs/) 和 [線上積木型錄](https://blocky.v7rc.io/docs/block-catalog.json)，依照公開規格生成或修改可匯入的工作區 XML。

### 安裝與啟用

1. 下載本範例庫。

   ```sh
   git clone https://github.com/v7rc/V7RC_Blockly_Examples.git
   cd V7RC_Blockly_Examples
   ```

2. 在 Codex 開啟這個資料夾作為專案，或在該目錄啟動 Codex CLI。Codex 會從 [專案內的 Skill 目錄](.agents/skills/v7rc-blockly-xml/) 載入這個 Skill。在輸入框輸入 `$v7rc-blockly-xml` 呼叫它。若未出現在選單，重新啟動 Codex 後再試。 [Codex Skill 載入規則](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

### 試用範例

把這段指令貼給 Codex：

```text
$v7rc-blockly-xml 幫我生成 canvas-hello.xml。
程式開始時顯示並清除圖層 0，然後在座標 (30, 50) 畫上黃色文字 Hello V7RC。
請使用公開積木型錄核對積木與插槽名稱，輸出完整可匯入的 Blockly 工作區 XML。
```

在 [V7RC Blockly 編輯器](https://blocky.v7rc.io/) 使用「匯入」選擇 `canvas-hello.xml`，確認初始化積木已載入。要看原生畫布效果，請在支援 Blockly 繪圖的 V7RC App 執行。


### 上傳到指定裝置

```text
$v7rc-blockly-xml 請把剛驗證完成的 XML 上傳到我的 V7RC 裝置。
Device ID：<你的 Device ID>
```

也可以提供含 `id` 的完整編輯器網址。未指定目標時，Skill 會請你提供 Device ID。上傳前會備份現有工作區，上傳後會讀回比對。Device ID 同時用作目前的儲存憑證，請避免公開分享。

## 使用 Claude Code

在倉庫根目錄執行 `claude`，再輸入 `/v7rc-blockly-xml` 加上需求。Claude Code 會從專案入口載入與 Codex 共用的指引和上傳腳本。 [`.claude/skills/v7rc-blockly-xml/`](.claude/skills/v7rc-blockly-xml/)
