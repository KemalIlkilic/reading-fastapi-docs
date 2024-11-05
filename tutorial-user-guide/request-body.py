from fastapi import FastAPI
from pydantic import BaseModel
"""
The function parameters will be recognized as follows:

 .If the parameter is also declared in the path, it will be used as a path parameter.
 .If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
 .If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
 
"""

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.get('/')
async def hello_world():
    return {'message': 'hello world'}


@app.post("/items/")
async def create_item(item: Item):
    return item
