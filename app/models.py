from pydantic import BaseModel

# todo: モデルをつくる(多分変わる)

class TagModel(BaseModel):
    category_id: str
    id_list: list