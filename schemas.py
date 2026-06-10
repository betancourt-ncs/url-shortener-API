from pydantic import BaseModel
from datetime import datetime


class URLCreate(BaseModel):
    url: str


class URLResponse(BaseModel):
    id: int
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class URLStatsResponse(URLResponse):
    access_count: int
