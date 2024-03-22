from .schema import UserCreateModel, UserCreateResponseModel
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_user_handler(request_body: UserCreateModel):
    try:
        user_service = UserService()
        created_user = user_service.create_user_and_save(request_body.name,request_body.min_price,request_body.max_price)
        response = UserCreateResponseModel(id=created_user.id, name=created_user.name,min_price=created_user.min_price,max_price=created_user.max_price)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())
