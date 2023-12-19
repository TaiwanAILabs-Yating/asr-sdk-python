
import requests
import json
import os
import yaml

class HttpClient:
  def __init__(self, key: str, config_path: str = None) -> None:
    self.key = key
    
    config = self.__read_api_url(config_path)
    self.base_uri = config['RESTfulAPI']['URL']
    self.polling_interval_secs = 3
  
  def __read_api_url(self, config_path: str):
    if config_path is None:
      path = os.path.abspath(__file__)
      config_path = os.path.dirname(path) + '/configs/api.yaml'
      
    with open(config_path, 'r') as config:
      return yaml.safe_load(config)
  
  def __build_headers(self) -> dict:
    return {
      'Key': self.key,
      'Content-Type': 'application/json',
    }
  
  def get(self, resource: str):
    try:
      headers = self.__build_headers()
      with requests.get(f'{self.base_uri}{resource}', headers=headers) as response:
        if response.status_code != 200:
          error = json.loads(response.text)["error"]
          raise Exception(f"http request failure: {error}")
        return json.loads(response.text)
    except Exception as err:
      raise err
  
  def post(self, resource: str, data: any):
    headers = self.__build_headers()
    try:
      with requests.post(f'{self.base_uri}{resource}', headers=headers, data=data) as response:
        if response.status_code != 200 and response.status_code != 201:
          error = json.loads(response.text)["error"]
          raise Exception(f"http request failure: {error}")
        return json.loads(response.text)
    except Exception as err:
      raise err