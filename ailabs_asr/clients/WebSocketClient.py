from .AbstractWebsocketClient import AbstractClient
import json

class Client(AbstractClient):
  def on_message(self, ws, message):
    msg = json.loads(message)
    if 'pipe' in msg:
      if 'verbose' in self.args:
        print(msg)
      elif 'asr_final' in msg['pipe']:
        start_time = float(msg['pipe']['asr_begin_time'])
        end_time = float(msg['pipe']['asr_end_time'])
        
        if ('translated_asr_sentence' in msg['pipe']):
          print(f'[{start_time:.2f} s - {end_time:.2f} s]',
            f'{msg["pipe"]["translated_asr_sentence"]}')
          
        print(f'[{start_time:.2f} s - {end_time:.2f} s]',
          f'{msg["pipe"]["asr_sentence"]}')
        
      if 'asr_eof' in msg['pipe'] and msg['pipe']['asr_eof']:
        if 'input_wav' in self.args:
          self._ws.close()
        elif 'audio_url' in self.args:
          self._ws.close()
    else:
      print(message)
