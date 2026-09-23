# S-053：演员工具开发基础能力核对

2026-09-12，Apple 官方文档检索摘要，未运行SDK示例。实现评估复用E-008，不推断竞品内部代码。

- [语音合成](https://developer.apple.com/documentation/avfoundation/speech-synthesis)：AVSpeechSynthesizer 可朗读文本；系统能力可作基础声音，不保证与高级TTS同等音质。
- [图像文字识别](https://developer.apple.com/documentation/vision/locating-and-displaying-recognized-text)：Vision 可识别图片文字；识字不等于可靠还原多栏剧本/角色/跨页顺序。
- [端侧语音识别能力](https://developer.apple.com/documentation/speech/sfspeechrecognizer/supportsondevicerecognition)：requiresOnDeviceRecognition 需支持标志为true，不假定所有语言设备可用。

未查厂商即时TTS单价、不提供美元成本承诺；开发工期属于基于功能拆分的工程估计，不是来源披露的竞品工期。
