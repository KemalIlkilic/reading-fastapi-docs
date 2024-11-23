from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    #Pydantic model için example gösteriyorsun.
    #it will be used in the API docs.
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

#When using Field() with Pydantic models, you can also declare additional examples:
class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])

"""
When using any of:
Path()
Query()
Header()
Cookie()
Body()
Form()
File()
you can also declare a group of examples with additional information that will be added to 
their JSON Schemas inside of OpenAPI.
"""

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results