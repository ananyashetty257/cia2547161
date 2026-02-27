from fastapi import FastAPI
import json
import os
from pydantic import BaseModel

app = FastAPI()

# Load database safely
if os.path.exists("app.json"):
    with open("app.json", "r") as f:
        db = json.load(f)
else:
    db = []

# Save database
def save_db():
    with open("app.json", "w") as f:
        json.dump(db, f, indent=4)

# Pydantic Model
class Item(BaseModel):
    id: int
    name: str
    price: int

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

@app.get("/items")
def get_items():
    return db

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items")
def add_item(item:Item):
    db.append(item.dict())
    save_db()
    return {"message": "Item added successfully", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(db):
        if existing_item["id"] == item_id:
            db[i] = item.dict()
            save_db()
            return {"message": "Item updated successfully", "item": item}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(db):
        if item["id"] == item_id:
            del db[i]
            save_db()
            return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}
