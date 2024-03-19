from .schema import RegisterPreferencesModel, PreferenceModel, UserCreateModel
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def register_preferences_handler(userId:str,request_body: UserCreateModel):
    try:
        """

        """
        response = {"response": "Successful Operation"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response)
