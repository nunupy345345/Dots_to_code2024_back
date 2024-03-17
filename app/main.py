import uvicorn
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
# MEMO ↓CORSを有効にしたいとき使う
# from fastapi_cors import CORS 
from models import CategoryModel
from data.item import read_google_form_tsv
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/category")
async def get_items_by_category(request_body: CategoryModel):
    """example
    requestBody:
    {
    "user_id":1243254,
    "category_list":["食品・スイーツ","趣味・ライフスタイル雑貨"]
    }
    response
    {
    "six_item_ids": [
        33,
        28,
        4,
        15,
        6,
        25
    ]
    }
    """
    try:
        user_id = request_body.user_id
        category_list = request_body.category_list
        item_list = []
        item_ids = []
        # COMMENT: tsvからitemを取ってくる
        item_list = read_google_form_tsv("./data/item_form.tsv")

        # COMMENT: itemsリストをループして、各アイテムのカテゴリが指定されたカテゴリリストに含まれているかどうかを確認
        for item in item_list:
            if item.category.value in category_list:
                # COMMENT: itemsのidをリストに追加
                item_ids.append(item.id)
        six_item_ids = random.sample(item_ids,6)
        
        # todo: userとカテゴリをDBに保存する
        response =  {"six_item_ids":six_item_ids}
    except Exception as e:
            # COMMENT: エラーが発生した場合はHTTP例外を発生させる
            raise HTTPException(status_code=500, detail=f"Error updating documents: {str(e)}")
    return JSONResponse(status_code=200, content=response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
