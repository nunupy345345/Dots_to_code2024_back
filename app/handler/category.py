from .schema.category import CategoryModel
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def category_handler(request_body: CategoryModel):
    try:
        user_id = request_body.user_id
        category_list = request_body.category_list

        # todo: ユーザーが選んだカテゴリを保存しておく(useridとcategoryidを紐づけて保存)

        response = {"response": "Successful Operation"}

    except Exception as e:
        # COMMENT: エラーが発生した場合はHTTP例外を発生させる
        raise HTTPException(status_code=500, detail=f"Error updating documents: {str(e)}")
    return JSONResponse(status_code=200, content=response)
