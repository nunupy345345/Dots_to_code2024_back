import sys
from pydantic import BaseModel, HttpUrl
from .category import Category


class Item(BaseModel):
    id: int
    name: str
    category: Category
    price: int
    url: HttpUrl
    image_url: HttpUrl
    evaluations: list[int]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
