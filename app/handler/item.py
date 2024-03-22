from .schema import ItemResponseModel,ItemModel
from services.item import ItemService
from services.user import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from domain import Category
from repository.user import UserRepository
import random

def send_items_handler(userId: str):
    try:
        """
        /items/{userId}で使用
        そのユーザーに好き嫌いを判定してもらうアイテムを6つ返す
        """
        us = UserService()
        items = us.get_preference_unregistered_items(userId)
        if len(items) < 6:
            item_models = [item.model_dump() for item in items]
        else:
            selected_items = random.sample(items, 6)

            # ItemModelのリストを作成
            item_models = []
            for item in selected_items:
                item_model = ItemModel(
                    id=item.id,
                    name=item.name,
                    category=item.category,
                    price=item.price,
                    url=item.url,
                    image_url=item.image_url,
                    evaluations=item.evaluations
                )
                item_models.append(item_model)

            # ItemResponseModelを作成
        response = ItemResponseModel(item_list=item_models)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error send items: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())