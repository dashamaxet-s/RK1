from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0)  
    tags: list[str] = Field(default_factory=list)


class ItemRead(ItemCreate):
    id: int


fake_db: dict[int, ItemRead] = {}
next_id = 1

# Эндпоинт
@app.post("/items", response_model=ItemRead, status_code=201)
def create_item(item: ItemCreate) -> ItemRead:
    global next_id
    
    new_item = ItemRead(id=next_id, **item.model_dump())
    
   
    fake_db[next_id] = new_item
    next_id += 1
    
    return new_item