from .schema import RecommendResponseModel
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from services.user import UserService

def recommend_handler(user_id: str):
    try:
        """
        response: RecommendResponseModel
        そのユーザーにおすすめする商品5つを返す
        評価が高いもの順
        """
        us = UserService()
        recommended_items = us.get_updated_user_recommend_items(user_id)
        response = recommended_items
        response = RecommendResponseModel(item_list=recommended_items)
        # response = {"status":"Successful Operation"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error recommend items: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())
