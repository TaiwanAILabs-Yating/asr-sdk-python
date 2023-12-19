from pathlib import Path
import sys
import asyncio
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import ailabs_asr.transcriber as t
from ailabs_asr.types import ModelConfig, TranscriptionConfig
from concurrent.futures import as_completed

audio = 'https://your-hostname.com/audio.mp3'

async def main():
  model = ModelConfig('asr-zh-en-std')
  config = TranscriptionConfig(True, True)
  c = t.Transcriber('api-key', model, config)
  multiple_tasks = []
  for _ in range(2):
    transcript = c.transcribe(audio)
    task = transcript.wait_for_completion_async()
    multiple_tasks.append(task)
    
  for task in as_completed(multiple_tasks):    
    print(task.result().transcript)

asyncio.run(main())


