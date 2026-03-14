from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define Item model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for items
items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# TODO: Implement CRUD endpoints for items
# - GET /items
# - POST /items
# - GET /items/{item_id}
# - PUT /items/{item_id}
# - DELETE /items/{item_id}

# Add your code here