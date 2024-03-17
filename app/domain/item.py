import sys
sys.path.append("~/app")
from pydantic import BaseModel, HttpUrl
from domain.category import Category


class Item(BaseModel):
    id: int
    name: str
    category: Category
    price: int
    url: HttpUrl
    image_url: HttpUrl
    evaluations: list[int]
