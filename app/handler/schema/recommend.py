from pydantic import BaseModel, Field


class RecommendResponseModel(BaseModel):
    recommend_list : list[str] = Field(..., min_items=5, max_items=5)
