from pydantic import BaseModel, Field, field_validator


class Post(BaseModel):
    title: str = ""
    text: str = Field(..., min_length=1)
    published: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
