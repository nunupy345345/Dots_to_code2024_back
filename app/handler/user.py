from .schema import UserCreateModel, UserCreateResponseModel
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_user_handler(request_body: UserCreateModel):
    try:
        user_service = UserService()
        created_user = user_service.create_user(request_body.name)
        response = UserCreateResponseModel(id=created_user.id, name=created_user.name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())
