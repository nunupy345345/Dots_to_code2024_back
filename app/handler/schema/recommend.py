from pydantic import BaseModel, Field

class RecommendResponseModel(BaseModel):
    RecommnedList: list[str] = Field(...,min_items=5, max_items=5)
    