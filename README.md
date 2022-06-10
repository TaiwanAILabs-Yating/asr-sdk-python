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
