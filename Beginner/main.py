from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"data": "Hello World!"}


class userPostIn(BaseModel):
    body: str


class UserPost(userPostIn):
    id: int


post_table = {}


@app.post("/user", response_model=UserPost)
async def create_post(post: userPostIn):
    data = post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
