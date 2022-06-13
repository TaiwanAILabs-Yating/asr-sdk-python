import yaml
import os
import requests
from .clients.WebSocketClient import Client

class StreamingClient:
  __websocket_url = ''
  __token_api_url = ''
  __key = ''
  __websocket_client = None
  
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
  
  def start_streaming_wav(
    self,
    pipeline: str,
    file: str,
    verbose: bool = False):
    
    token = self.__generate_token(pipeline)
    self.__websocket_client = Client({
      'websocket_url': self.__websocket_url,
      'input_wav': file,
      'verbose': verbose
    })
    
    self.__websocket_client.init_websocket(token)
    self.__websocket_client.run()
  
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
  
  def setHandler(self, on_processing_sentence = None, on_final_sentence = None):
    if on_processing_sentence:
      self.__websocket_client.on_processing_sentence = on_processing_sentence
    if on_final_sentence:
      self.__websocket_client.on_final_sentence = on_final_sentence
