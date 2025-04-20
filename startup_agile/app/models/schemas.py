from pydantic import BaseModel
from typing import Optional

class RankRequest(BaseModel):
    resume: str
    job_description: str
    photo: Optional[str] = None

class RankResponse(BaseModel):
    score: int
    feedback: str
    photo_check: Optional[str] = None
