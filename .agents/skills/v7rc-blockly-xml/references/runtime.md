# V7RC native runtime notes

## Camera and drawing

- `v7rc_camera_take_photo` requests the App's camera image. Pair it with the top-level `v7rc_screen_capture_feedback` event and its `DO` statement. The current generator binds the received image to the fixed `screen_image_data` variable of Blockly type `String`. Declare a variable with that name and type when reading it. The separate screen-capture action may include App UI.
- Use `v7rc_show_canvas_layer` before drawing into the same layer. The tested iOS layout starts with its drawing layers hidden. Use the App model and camera permissions appropriate to the requested runtime.
- Treat millisecond delays as timing choices that may need target testing. In the tested iOS workflow, opening the camera and immediately starting detection can race camera initialization.

## Object detection

- `v7rc_ai_object_detection_enable` uses the App's object-detection model catalog. Use the catalog's `__none__` placeholder if the user has not selected a real model, and tell them to select one in the App. Never invent catalog entries.
- `v7rc_receive_ai_parse_each_item` supplies fixed Blockly `String` variables `ai_object_id`, `ai_object_type`, `ai_object_location_x`, `ai_object_location_y`, `ai_object_width`, `ai_object_height`, and `ai_object_confidence`. Coordinates, index, dimensions, and confidence are numeric in the generated callback. The separate top-level `v7rc_receive_ai_data` callback exposes the fixed count `ai_qty`.
- The inspected runtime calls the per-item handler first, with an index starting at zero, then the whole-frame handler. For overlays, clear on the first item before drawing, and also clear in the whole-frame handler when the count is zero. Confirm that the target App actually sends empty-frame events.
- To format confidence from a fraction as one decimal place in percent using stock blocks, round confidence × 1000 to integer tenths, divide by ten and floor for the whole part, and use `math_modulo` for the final digit. Join the name, decimal separator, digit, and percent sign.
- The [published object detection example](https://github.com/v7rc/V7RC_Blockly_Examples/tree/main/camera-object-detection) contains the complete percent-formatted XML and two diagnostic workspaces.

## Microduck

- Use the camera callback to verify image capture before adding image AI or SRT motion. The App bridge, model service, and robot or simulator can fail independently. Verify the requested control profile and timing in the target environment. Keep simulator navigation results separate from physical-device acceptance.


## iOS 語音對話

The public 1.1.0 catalog has no `MODE` field on `v7rc_voice_recorder_enable`. When targeting a compatible iOS test build, use the shipped [v3 and Canvas v4 examples](../../../../voice-chatbot/README.md) as editor-verified references for `CONVERSATION` and `CONVERSATION_CANVAS`. Older editor exports can drop the field. Preserve it during upload and validate against the target App’s bundled editor.
