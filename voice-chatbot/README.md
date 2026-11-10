# V7RC 語音對話範例

- [自動對話 v3](v7rc-voice-chatbot-hands-free-v3.xml) 會顯示問句和正在朗讀的句子，最後一句播完後恢復收音。
- [Canvas v4](v7rc-voice-chatbot-hands-free-canvas-v4.xml) 把問句和正在朗讀的句子繪製到 Canvas 1，每句播完清除字幕。最後一句播完後才恢復收音。

請在支援相應模式的 iOS V7RC 測試版內建 Blockly 匯入 XML，並確認已下載可用的本機 LLM。執行後點麥克風開始，對話期間可再點一次關閉自動收音。若已用 Skill 上傳到裝置，在 App 內下載雲端工作區後重新執行。

公開型錄 1.1.0 尚未列出收音積木的 `MODE`。這兩份範例分別需要內建編輯器與 App 支援 `CONVERSATION` 和 `CONVERSATION_CANVAS`。舊版編輯器可能在匯出時丟棄欄位。
