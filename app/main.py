from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  id: int
  name: str
  description: str

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
  return {"item_id": item_id, "q": q}

@app.post("/items")
def post_item(item_id: int, item: Item):
  return {"qid": item_id, "item": item.dict()}