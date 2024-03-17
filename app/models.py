from pydantic import BaseModel

# todo: モデルをつくる(多分変わる)

class CategoryModel(BaseModel):
    user_id: int
    category_list: list
    
    