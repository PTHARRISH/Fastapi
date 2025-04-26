import asyncio
from typing import Union
# Union is part of Python’s type hinting system (available since Python 3.5), 
# and it means "this value can be one type OR another."

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# It is built on top of Starlette for the web parts and Pydantic for the data parts.
# FastAPI is a web framework for building APIs with Python 3.6+ based on standard Python type hints.
from fastapi import FastAPI

# this is a instance of FastAPI
app = FastAPI()


# this is a decorator that tells FastAPI what URL should call the function
@app.get("/")
def read_root():
    return {"Hello": "World"}


# using Union to specify that the query parameter q can be either a string or None
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# cleaner way to use Union is to use the pipe operator |, which is available in Python 3.10 and later.
@app.get("/price/{price_id}")
def read_price(price_id: int, q: str | None = None ):
    return {"price_id": price_id, "q": q}



@app.get("/slow")
async def slow_route():
    await asyncio.sleep(2)  # Simulates slow operation
    return {"message": "Thanks for waiting!"}