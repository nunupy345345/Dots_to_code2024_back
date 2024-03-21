from .schema.category import CategoryModel
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from repository.user import UserRepository


def category_handler(request_body: CategoryModel):
    try:
        user_id = request_body.user_id
        category_list = request_body.category_list
        category_service = UserService()
        category_service.register_item_category(user_id, category_list)
        response = {"response": "Successful Operation"}
     
    except Exception as e:
        # COMMENT: エラーが発生した場合はHTTP例外を発生させる
        raise HTTPException(status_code=500, detail=f"Error register category: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())
