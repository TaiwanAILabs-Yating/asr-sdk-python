# AILabs ASR Python software development kit

[![PyPI](https://img.shields.io/pypi/v/ailabs-asr?color=blue)](https://pypi.org/project/ailabs-asr/) ![PyPI - License](https://img.shields.io/pypi/l/ailabs-asr)

## Development Environment

- Python 3.9

```bash
# install portaudio first if you develop on MAC OS X
brew install portaudio

pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' -r requirements_dev.txt

# please check PyAudio site: https://people.csail.mit.edu/hubert/pyaudio/
# if you encouter some issues while installing PyAudio
```

## Installation

```bash
pip install ailabs-asr
```

## Samples

```python
# init the streaming client
asr_client = StreamingClient('api-key-applied-from-devconsole')

# start streaming with wav file
asr_client.start_streaming_wav(
  pipeline='asr-zh-en-std',
  file='voice.wav'
  verbose=False, # enable verbose to show detailed recognition result
  on_processing_sentence=on_processing_sentence,
  on_final_sentence=on_final_sentence)

# without file to start streaming with the computer's microphone
asr_client.start_streaming_wav(
  pipeline='asr-zh-en-std',
  on_processing_sentence=on_processing_sentence,
  on_final_sentence=on_final_sentence)
```

:bulb: `start_streaming_wav()` method allow users to provide callback function to handle the recognition result see the result format [below](#message-format)

:bulb: lookup the available pipelines in [the next section](#support-languagepipeline)

:bulb: see more samples in the [sample respository](https://github.com/TaiwanAILabs-Yating/asr-python-sample)

## Support Language(`pipeline`)

| pipeline      | Info                                                 | language               |
| ------------- | ---------------------------------------------------- | ---------------------- |
| asr-zh-en-std | Use it when speakers speak Chinese more than English | Mandarin and English   |
| asr-zh-tw-std | Use it when speakers speak Chinese and Taiwanese.    | Mandarin and Taiwanese |
| asr-en-std    | English                                              | English                |
| asr-jp-std    | Japanese                                             | Japanese               |

## Message Format

There are 2 kinds of recognized result:

### The Processing Sentence(Segment)

```json
{
  "asr_sentence": "範例句子"
}
```

### The Final Sentence(Complete Sentence)

```json
{
  "asr_final": true,
  "asr_begin_time": 9.314,
  "asr_end_time": 11.314,
  "asr_sentence": "完整的範例句子",
  "asr_confidence": 0.5263263653207881,
  "asr_word_time_stamp": [
    {
      "word": "完整的",
      "begin_time": 9.74021875,
      "end_time": 10.100875
    },
    {
      "word": "範例句子",
      "begin_time": 10.100875,
      "end_time": 10.1664375
    }
  ],
  "text_segmented": "完整的 範例句子"
}
```
