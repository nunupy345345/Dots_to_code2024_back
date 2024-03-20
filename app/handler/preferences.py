from .schema import RegisterPreferencesModel, PreferenceModel
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def register_preferences_handler(user_id: str, request_body: RegisterPreferencesModel):
    try:
        """
        ユーザーの各アイテムの好みを登録する
        """
        us = UserService()
        # for item in request_body.PreferenceList:
        us.register_user_preferences(user_id,request_body)
        response = {"response": "Successful Operation"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response)
