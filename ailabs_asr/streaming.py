import yaml
import os
import requests
import websocket
from .clients.WebSocketClient import Client

class StreamingClient:
  __websocket_url = ''
  __token_api_url = ''
  __key = ''
  
  def __init__(
    self,
    key: str,
    config_path: str = None) -> None:
    
    config = self.__read_api_url(config_path)
    self.__key = key
    self.__websocket_url = config['WebSocket']['URL']
    self.__token_api_url = config['TokenAPI']['URL']
  
  def __read_api_url(self, config_path: str):
    if config_path is None:
      path = os.path.abspath(__file__)
      config_path = os.path.dirname(path) + '/configs/api.yaml'
      
    with open(config_path, 'r') as config:
      return yaml.safe_load(config)
  
  def start_streaming_wav(self, pipeline: str, file: str, verbose: bool = False):
    token = self.__generate_token(pipeline)
    websocket_client = Client({
      'input_wav': file,
      'verbose': verbose
    })
    
    websocket_client.ws = websocket.WebSocketApp(
      f'{self.__websocket_url}?token={token}',
      on_message=websocket_client.on_message,
      on_error=websocket_client.on_error,
      on_close=websocket_client.on_close,
      on_open=websocket_client.on_open
    )
    
    websocket_client.ws.run_forever()
  
  def __generate_token(self, pipeline: str):
    body = {
        'pipeline': pipeline,
    }
    res = requests.post(self.__token_api_url,
                        json=body,
                        headers={'key': self.__key},
                        verify=True)
    token = res.json()['auth_token']
    if len(token) == 0:
        print(res.text)
        exit(1)
    return token
  

def stream_file(key: str, pipeline: str, input_wav: str, verbose: bool = False, config_path: str = None):
  """
  ASR streaming to transcribe the voice to text
  
  Args:
      key (str): the key applied in dev-console
      config_path (str): assign API URL for testing
  Returns:
      None
  """
  asr_client = StreamingClient(key, config_path)
  asr_client.start_streaming_wav(pipeline, input_wav, verbose)
