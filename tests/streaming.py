from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from ailabs_asr.streaming import StreamingClient

asr_client = StreamingClient('9c5542d34a59f87f45659ab33d5ccbb9bdaec68d')
asr_client.start_streaming_wav('asr-stream-general', 'unorder-stream.wav')