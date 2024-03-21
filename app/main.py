import os
import uvicorn
from fastapi import FastAPI

# MEMO ↓CORSを有効にしたいとき使う
# from fastapi_cors import CORS
from handler.schema import CategoryModel, UserCreateModel, UserCreateResponseModel, RegisterPreferencesModel, \
    RecommendResponseModel, ItemResponseModel
from handler import category_handler, create_user_handler, register_preferences_handler, recommend_handler, send_items_handler

app = FastAPI()

if os.environ.get("ENV") == "production":
    os.sys.path.append("/app")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user", response_model=UserCreateResponseModel)
async def create_user(request_body: UserCreateModel):
    """
    ユーザーを作成する
    """
    return create_user_handler(request_body)


@app.post("/user/{user_id}/preferences")
async def register_preferences(user_id, request_body: RegisterPreferencesModel):
    """
    ユーザーの嗜好を登録する
    responseは200OKに
    e.g
    {
    "preference_list":[{"item_id":11,"is_like":true},{"item_id":5,"is_like":true}]
    }
    """
    return register_preferences_handler(user_id, request_body)


@app.post("/category")
async def get_items_by_category(request_body: CategoryModel):
    """
    ユーザーが選んだカテゴリを保存しておく(useridとcategoryidを紐づけて保存)
    MEMO: ルーター部分には具体的な処理は書かない。処理はhandlerに書く
    e.g.
    {
    "user_id":"08f742ab-be3c-4e25-8329-e6d7b2696aef",
    "category_list":["cosme_beauty","food_sweet"]
    }
    """
    return category_handler(request_body)


@app.get("/user/{user_id}/recommend", response_model=UserCreateResponseModel)
async def recommend(user_id):
    """
    そのユーザーにおすすめする商品
    requestbody:無し
    """
    return recommend_handler(user_id)

@app.get("/items/{user_id}", response_model=ItemResponseModel)
async def send_items(user_id:str):
    """
    そのユーザーに好き嫌いを判定してもらうアイテムを返す
    requestbody:無し
    e.g http://localhost:8000/items/:user_id
    で、Path VariablesにKey:user_id,Value:08f742ab-be3c-4e25-8329-e6d7b2696aef
    """
    return send_items_handler(user_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
