from .schema import RecommendResponseModel,RecommendItemModel
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
        recommend_items = us.get_updated_user_recommend_items(user_id)
        recommend_item_models = []
        for item in recommend_items:
            recommend_item_model = RecommendItemModel(
                id=item.id,
                name=item.name,
                category=item.category,
                price=item.price,
                url=str(item.url),
                image_url=item.image_url,
                evaluations=item.evaluations
            )
            recommend_item_models.append(recommend_item_model)
        response = RecommendResponseModel(recommend_list=recommend_item_models)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error recommend items: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())
