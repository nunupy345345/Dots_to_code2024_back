import os
import uvicorn
from fastapi import FastAPI

# MEMO ↓CORSを有効にしたいとき使う
# from fastapi_cors import CORS
from handler.schema import CategoryModel, UserCreateModel, UserCreateResponseModel
from handler import category_handler, create_user_handler

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


@app.post("/category")
async def get_items_by_category(request_body: CategoryModel):
    """
    MEMO: ルーター部分には具体的な処理は書かない。処理はhandlerに書く
    """
    return category_handler(request_body)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
