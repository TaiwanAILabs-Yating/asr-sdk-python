from .AbstractWebsocketClient import AbstractClient
import json

class Client(AbstractClient):
  def _on_message(self, ws, message):
    msg = json.loads(message)
    if 'pipe' in msg:
      if 'verbose' in self.args and self.args['verbose'] == True:
        print(msg)
      
      if 'asr_sentence' in msg['pipe']:
        self._handle_asr_result(msg['pipe'])
        
      if 'asr_eof' in msg['pipe'] and msg['pipe']['asr_eof']:
        if 'input_wav' in self.args:
          self._ws.close()
        elif 'audio_url' in self.args:
          self._ws.close()
    else:
      print(message)
