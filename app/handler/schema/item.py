from pydantic import BaseModel, UUID4, HttpUrl, Field

class ItemModel(BaseModel):
    id: int
    name: str
    category: str
    price: int
    url: HttpUrl
    image_url: HttpUrl
    evaluations: list[int]
    
class ItemResponseModel(BaseModel):
    ItemList : list[ItemModel]