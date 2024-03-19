from pydantic import BaseModel, UUID4
from typing import Optional
from .item import Item
from .category import Category


class User(BaseModel):
    id: UUID4
    name: str
    selected_category: Optional[set[Category]] = None
    preferences: Optional[set[tuple[Item, bool]]] = None
    recommended_items: Optional[list[Item]] = None
