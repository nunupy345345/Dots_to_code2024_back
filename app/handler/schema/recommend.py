from pydantic import BaseModel, Field,HttpUrl

class RecommendItemModel(BaseModel):
    id: int
    name: str
    category: str
    price: int
    url: HttpUrl
    image_url: HttpUrl
    evaluations: list[int]
    
class RecommendResponseModel(BaseModel):
    recommend_list : list[RecommendItemModel]
    #  = Field(..., min_items=5, max_items=5)
