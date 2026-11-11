# V7RC_Blockly_Examples

[繁體中文](README.md) · [简体中文](README.zh-CN.md) · [English](README.en.md) · [日本語](README.ja.md)

V7RC Blockly のプログラミングサンプル集です。

## サンプル

- [`blockly_translation.xml`](blockly_translation.xml) · スマートフォンのマイクで中国語を英語に翻訳して表示
- [`blockly-llm-louis-2025-02-10.xml`](blockly-llm-louis-2025-02-10.xml) · チャットボットの試作
- [`blockly_AI-mqtt.xml`](blockly_AI-mqtt.xml) · AI と MQTT の連携
- [`blockly_GPS_sample.xml`](blockly_GPS_sample.xml) · スマートフォンの GPS を取得
- [`blockly_Gyro.xml`](blockly_Gyro.xml) · スマートフォンのジャイロセンサーを取得
- [`blockly_v7rc_lego_racing.xml`](blockly_v7rc_lego_racing.xml) · Legi シリーズの車両を操作
- [`blockly_robot_control.xml`](blockly_robot_control.xml) · 益成先生のロボットを操作
- [`camera-object-detection/README.md`](camera-object-detection/README.md) · カメラで物体を検出し、枠、名前、信頼度を小数第1位までのパーセントで表示
- [`voice-chatbot/README.md`](voice-chatbot/README.md) · 音声対話 v3 と Canvas v4。文ごとに読み上げ、終了後に録音を再開。Canvas v4 では字幕をキャンバスに描画し、読み上げ後に消去

## Codex で Blockly XML を生成

```sh
git clone https://github.com/v7rc/V7RC_Blockly_Examples.git
cd V7RC_Blockly_Examples
```

クローンしたリポジトリを Codex で開くか、リポジトリのディレクトリで Codex CLI を起動してください。プロジェクトのスキルは次の入力で呼び出せます。 `$v7rc-blockly-xml`

```text
$v7rc-blockly-xml canvas-hello.xml を生成してください。レイヤー 0 を消去し、座標 (30, 50) に黄色で Hello V7RC を描画してください。
```

エディターで XML をインポートしてください。キャンバスのサンプルは描画に対応する V7RC アプリで実行してください。 [エディター](https://blocky.v7rc.io/)

[開発者向けドキュメント](https://blocky.v7rc.io/docs/) · [ブロックカタログ](https://blocky.v7rc.io/docs/block-catalog.json) · [スキルのディレクトリ](.agents/skills/v7rc-blockly-xml/)

## 指定したデバイスにアップロード

```text
$v7rc-blockly-xml 検証済みの XML を Device ID <お使いの Device ID> にアップロードしてください。
```

id を含むエディターの URL も指定できます。スキルは既存のワークスペースをバックアップし、アップロード後に読み戻して確認します。Device ID は公開しないでください。
