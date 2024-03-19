from .schema import RecommendResponseModel
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def recommend_handler(userId:str):
    try:
        """
        response: RecommendResponseModel
        """
        response = {"response": "Successful Operation"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response)
