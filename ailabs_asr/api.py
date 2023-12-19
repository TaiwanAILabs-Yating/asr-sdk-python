from .types import TranscriptionConfig, ModelConfig
from .client import HttpClient
import json

def get_transcription(client: HttpClient, transcription_id) -> str:
  resource = f'/transcriptions/{transcription_id}'
  return client.get(resource)

def post_transcription(
  client: HttpClient,
  audio_url: str,
  model: ModelConfig,
  config: TranscriptionConfig,
):
  resource = f'/transcriptions'
  body = __generate_body(audio_url, model, config)
  return client.post(resource, body)[0]
  
def __generate_body(
  audio_url: str,
  model: ModelConfig,
  config: TranscriptionConfig,
) -> str:
  return json.dumps({
    'audioUri': audio_url,
    'modelConfig': model.toDict(),
    'featureConfig': config.toDict()
  })
  