from typing_extensions import Self
from typing import Optional
import concurrent.futures
import time
from .types import ModelConfig, TranscriptionConfig, TranscriptionStatus
from .api import post_transcription, get_transcription
from .client import HttpClient

class Transcript:
  def __init__(
    self,
    transcription_id: str,
    client: HttpClient,
  ) -> None:
    self.transcription_id = transcription_id
    self.client = client
    self._executor = concurrent.futures.ThreadPoolExecutor()
    self.result = None
    
  @property
  def status(self):
    if self.result:
      return self.result['status']
    response = get_transcription(self.client, self.transcription_id)
    status = TranscriptionStatus(response['status'])
    if status.is_done():
      self.result = response
    return status.text()
  
  @property
  def transcript(self) -> str:
    if self.result:
      if 'sentences' in self.result:
        return self.result['sentences']
      else:
        return self.result
    response = get_transcription(self.client, self.transcription_id)
    if 'sentences' not in response:
      return '{}'
    return response['sentences']
  
  def wait_for_completion(self) -> Self:
    while True:
      response = get_transcription(self.client, self.transcription_id)
      status = TranscriptionStatus(response['status'])
      
      if status.is_done():
        self.result = response
        break
      time.sleep(self.client.polling_interval_secs)
    return self
      
  def wait_for_completion_async(
    self,
  ) -> concurrent.futures.Future[Self]:
    # return asyncio.to_thread(self.wait_for_completion)
    return self._executor.submit(self.wait_for_completion)

class Transcriber:
  def __init__(
    self,
    api_key: str,
    model: ModelConfig,
    config: TranscriptionConfig
  ) -> None:
    self.config = config
    self.model = model
    self.client = HttpClient(api_key)
  
  def transcribe(
    self,
    audio_url: str,
    config: Optional[TranscriptionConfig] = None,
  ) -> Transcript:
    if not self.model.validate():
      raise Exception(f'Model: {self.model.model} is not supported')
    
    if not config:
      config = self.config
    response = post_transcription(self.client, audio_url, self.model, config)
    transcription_id = response['uid']
    print(f"[ {transcription_id} ] Send task success")
    
    return Transcript(transcription_id, self.client)
  