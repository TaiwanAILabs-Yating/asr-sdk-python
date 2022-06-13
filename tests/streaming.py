from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from ailabs_asr.streaming import StreamingClient


def on_processing_sentence(message):
  print(f'hello: {message["pipe"]["asr_sentence"]}')

def on_final_sentence(message):
  print(f'world: {message["pipe"]["asr_sentence"]}')

asr_client = StreamingClient('9c5542d34a59f87f45659ab33d5ccbb9bdaec68d')
asr_client.start_streaming_wav(
  pipeline='asr-stream-general',
  file='unorder-stream.wav',
  on_processing_sentence=on_processing_sentence,
  on_final_sentence=on_final_sentence)