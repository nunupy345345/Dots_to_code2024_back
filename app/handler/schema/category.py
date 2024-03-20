from pydantic import BaseModel, UUID4

class CategoryModel(BaseModel):
    user_id: UUID4
    category_list: list[str]
