from pydantic import BaseModel, UUID4
from .item import Item
from .category import Category


class User(BaseModel):
    id: UUID4
    name: str
    selected_category: set[Category]
    preferences: set[tuple[Item, bool]] | None
    recommended_items: list[Item] | None
