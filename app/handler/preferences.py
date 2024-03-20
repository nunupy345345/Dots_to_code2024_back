from .schema import RegisterPreferencesModel, PreferenceModel
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def register_preferences_handler(user_id: str, request_body: RegisterPreferencesModel):
    try:
        """
        
        """
        response = {"response": "Successful Operation"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error register preferences: {str(e)}")
    return JSONResponse(status_code=200, content=response)
