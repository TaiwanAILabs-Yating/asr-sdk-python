from abc import ABC
import wave
from pyaudio import PyAudio, paComplete, paContinue, paInt16
import json

class AbstractClient(ABC):
  def __init__(self, args):
    self.args = args
    self.pa = None
    self.stream = None
    self.wave_file = None
    self._ws = None

  @property
  def ws(self):
      return self._ws

  @ws.setter
  def ws(self, ws):
      self._ws = ws

  @ws.getter
  def ws(self):
      return self._ws

  def create_stream(self):
    pa = self.pa
    if 'input_wav' in self.args:
      input_wav = self.args['input_wav']
      self.wave_file = wave.open(input_wav, 'rb')
      return pa.open(format=paInt16, channels=1, rate=16000, output=True,
                      stream_callback=self.cb_wav)
    else:
      return pa.open(format=paInt16, channels=1, rate=16000, input=True,
                      stream_callback=self.cb)

  def on_message(self, ws, message):
      pass

  def on_error(self, ws, error):
      print(error)

  def on_close(self, ws):
      if self.stream:
          self.stream.stop_stream()
          self.stream.close()
      if self.pa:
          self.pa.terminate()
      if self.wave_file:
          self.wave_file.close()
      print("### closed ###")

  def on_open(self, ws):
    if 'audio_url' not in self.args:
        self.pa = PyAudio()
        self.stream = self.create_stream()
        if 'j2' not in self.args:
          self.stream.start_stream()
          print("### start stream ###")
    print("### opened ###")

  def cb(self, in_data, frame_count, time_info, status_flags):
      self.ws.send(in_data, opcode=0x2)
      if in_data:
          print(in_data)
      return (in_data, paContinue)

  def cb_wav(self, in_data, frame_count, time_info, status_flags):
      if in_data:
          print(len(in_data))
      data = self.wave_file.readframes(frame_count)
      self.ws.send(data, opcode=0x2)

      if frame_count * 2 > len(data):
          self.ws.send('', opcode=0x2)
          return (data, paComplete)
      return (data, paContinue)
  
  def lang_switch(self, lang_code):
      print(f'lang switch: {lang_code}')
      data = {
              'pipe': {
                  'config': {
                      'liveStreamingCodeSwitch': lang_code
                  }
              } 
      }
      self.ws.send(json.dumps(data))
