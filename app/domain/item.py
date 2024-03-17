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
