from typing import Optional
class TranscriptionConfig(dict):
  def __init__(
    self,
    punctuator: bool = True,
    speaker_diarization: Optional[bool] = False,
    speakers_count: Optional[int] = 0,
    sentiment_analysis: Optional[bool] = False,
  ) -> None:
    self.punctuate = punctuator
    self.speaker_relabel = speaker_diarization
    self.speakers_expected = speakers_count
    self.sentiment_analysis = sentiment_analysis
  
  def toDict(self) -> dict:
    return {
      'punctuation': True,
      'speakerDiarization': self.speaker_relabel,
      'speakerCount': self.speakers_expected,
      'sentiment': self.sentiment_analysis,
    }

class TranscriptionStatus:
  pending = "pending"
  ongoing = "ongoing"
  completed = "completed"
  expired = "expired"
  error = "error"
  
  def __init__(self, status: str) -> None:
    self.status = status
  
  def text(self) -> str:
    return self.status

  def is_done(self):
    if self.status in (
      self.completed,
      self.error,
      self.expired,
    ):
      return True
    return False


class ModelConfig():
  __SUPPORT_MODELS = [
    "asr-zh-en-std",
    "asr-zh-tw-std",
    "asr-en-std",
  ]
  
  def __init__(
    self,
    model: str,
    customize_language_model: Optional[str] = "",
  ) -> None:
    self.model = model
    self.customlm = customize_language_model
    
  def validate(self):
    return self.model in self.__SUPPORT_MODELS
  
  def toDict(self) -> dict:
    return {
      'model': self.model,
      'customLm': self.customlm,
    }