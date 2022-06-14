from abc import ABC, abstractclassmethod

class ASRResultHandleStrategy(ABC):
  def __init__(self) -> None:
    super().__init__()
    
  @abstractclassmethod
  def on_processing_sentence(self, message):
    pass
  @abstractclassmethod
  def on_final_sentence(self, message):
    pass
  
class DefaultASRResultHandleStrategy(ASRResultHandleStrategy):
  def on_processing_sentence(self, message):
    print(f'segment: {message["asr_sentence"]}')
    
  def on_final_sentence(self, message):
    start_time = float(message['asr_begin_time'])
    end_time = float(message['asr_end_time'])
    if ('translated_asr_sentence' in message):
      print(f'[{start_time:.2f} s - {end_time:.2f} s]',
        f'{message["translated_asr_sentence"]}')
      
    print(f'[{start_time:.2f} s - {end_time:.2f} s]',
      f'{message["asr_sentence"]}')
