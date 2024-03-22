from pydantic import BaseModel, UUID4
from typing import Optional
from .item import Item
from .category import Category


class User(BaseModel):
    id: UUID4
    name: str
    min_price: int
    max_price: int
    selected_category: Optional[set[Category]] = None
    preferences: Optional[dict[int, bool]] = None
    recommended_items: Optional[list[Item]] = None

    @staticmethod
    def create(user_id: UUID4, name: str, min_price: int, max_price: int):
        return User(id=user_id, name=name,min_price=min_price,max_price=max_price)
