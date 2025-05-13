from pydantic import BaseModel
from typing import List


class ThoughtRequest(BaseModel):
    thought: str


class DistortionResponse(BaseModel):
    distortions_detected: List[str]
