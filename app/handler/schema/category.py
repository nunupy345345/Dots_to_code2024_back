from pydantic import BaseModel, UUID4


# todo: モデルをつくる(多分変わる)

class CategoryModel(BaseModel):
    user_id: UUID4
    category_list: list[str]
