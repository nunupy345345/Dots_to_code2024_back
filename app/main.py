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
    try:
        user_id = request_body.user_id
        category_list = request_body.category_list

        # todo: ユーザーが選んだカテゴリを保存しておく(useridとcategoryidを紐づけて保存)
        
        response = {"response": "Successful Operation"}
        
    except Exception as e:
            # COMMENT: エラーが発生した場合はHTTP例外を発生させる
            raise HTTPException(status_code=500, detail=f"Error updating documents: {str(e)}")
    return JSONResponse(status_code=200, content=response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
