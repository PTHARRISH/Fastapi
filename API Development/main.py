import asyncio
from typing import Union
# Union is part of Python’s type hinting system (available since Python 3.5), 
# and it means "this value can be one type OR another."

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# It is built on top of Starlette for the web parts and Pydantic for the data parts.
# FastAPI is a web framework for building APIs with Python 3.6+ based on standard Python type hints.
from fastapi import FastAPI
from pydantic import BaseModel
# Pydantic is a data validation and settings management library for Python, which uses Python type annotations.


# this is a instance of FastAPI
app = FastAPI(
    title="My First FastAPI App",
    description="This is my first FastAPI app. It is a simple API that returns a greeting message.",
)


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



# asynchronous function to handle slow operations
# FastAPI supports asynchronous programming, which allows you to write non-blocking code using async and await keywords.
@app.get("/slow")
async def slow_route():
    await asyncio.sleep(2)  # Simulates slow operation
    return {"message": "Thanks for waiting!"}


#post method in fastapi
products = []

class Item(BaseModel):
    name: str
    price: int
    is_offer: bool | None = None  # Optional field with default value
    description: str | None = None  # Optional field with default value
    
@app.post("/items/")
def create_item(data: Item):
    # return {"item_name": data.name, "item_price": data.price, "is_offer": data.is_offer, "description": data.description}
    # return data.dict()  # Convert the Pydantic model to a dictionary and return it as JSON
    # return data  # Return the Pydantic model directly, FastAPI will convert it to JSON automatically
    # return data.json() # Convert the Pydantic model to JSON string and return it
    # return data.name # return the name of the item only
    return data.name, data.price, data.is_offer, data.description # return the name, price, is_offer and description of the item it store in a list 
    
    
 # temporary list to store the products
# products = [] # this is a list to store the products
# this is a class to define the Item model   
@app.post("/create_product/")
def create_product(item: Item):
    product_details = {"name": item.name, "price": item.price, "is_offer": item.is_offer, "description": item.description} # create a dictionary with the product description
    products.append(product_details) # append the product details to the products list
    return {"message": "Product created successfully", "product": products} # return a message and the products list
    # return {"message": "Product created successfully", "product": product_details} # return a message and the product details


@app.get("/view_products/")
def view_products():
    return {"products": products}
