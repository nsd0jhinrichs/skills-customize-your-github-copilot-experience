from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST Assignment")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    category: str = Field(min_length=1)
    price: float = Field(gt=0)


items = [
    {"id": 1, "name": "Example Book", "category": "books", "price": 12.99},
]
next_id = 2


@app.get("/")
def read_root():
    return {"message": "Welcome! Your FastAPI server is running."}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", status_code=201)
def create_item(payload: ItemCreate):
    global next_id

    new_item = {
        "id": next_id,
        "name": payload.name,
        "category": payload.category,
        "price": payload.price,
    }

    items.append(new_item)
    next_id += 1
    return new_item


# Optional stretch: add PUT /items/{item_id} and DELETE /items/{item_id}
