from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated,Literal

app = FastAPI()

class FilterParams(BaseModel):
    # Limit between 1-100, defaults to 100
    limit : int = Field(100, gt= 0,le=100)
    offset: int = Field(0, ge=0)
    #Must be either "created_at" or "updated_at", defaults to "created_at"
    order_by : Literal["created_at", "updated_at"] = "created_at"
    tags : list[str] = []

"""
When you make a GET request to /items/, you can provide query parameters like:
/items/?limit=50&offset=10&order_by=updated_at&tags=tag1&tags=tag2

Response:
{
    "limit": 50,
    "offset": 10,
    "order_by": "updated_at",
    "tags": ["tag1", "tag2"]
}
"""
@app.get('/items/')
async def read_items(filter_query : Annotated[FilterParams, Query()]):
    return filter_query