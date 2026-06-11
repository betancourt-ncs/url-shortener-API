from pydantic import BaseModel
from datetime import datetime


# What the client sends when creating or updating a short URL:
class URLCreate(BaseModel):
    url: str


# What the API sends back:
class URLResponse(BaseModel):
    id: int
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Stats endpoint
class URLStatsResponse(URLResponse):
    access_count: int
