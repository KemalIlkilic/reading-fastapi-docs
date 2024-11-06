from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

#by giving default value = None , we are making that q optional.
# !!!   = None !!! ile.
#str | None,that part just gives type hints.It can be string or None.
#It does not tell to fastapi that this q parameter is optional.
@app.get("/items/")
async def read_items(q : Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



@app.get("/items-pattern/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



#Having a default value of any type, including None, makes the parameter optional (not required).
@app.get("/items-default/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



#we can make the q query parameter required just by not declaring a default value
#q: str


#Query parameter list / multiple values¶
#When you define a query parameter explicitly with Query
#You can also declare it to receive a list of values, or said in another way, to receive multiple values.

@app.get("/items-multiple/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
#To declare a query parameter with a type of list, like in the example above
#you need to explicitly use Query, otherwise it would be interpreted as a request body.
"""
Then, with a URL like:
http://localhost:8000/items/?q=foo&q=bar

So, the response to that URL would be:
{
  "q": [
    "foo",
    "bar"
  ]
}
"""