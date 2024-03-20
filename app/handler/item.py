from .schema import ItemResponseModel
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
        # items = []
        us = UserService()
        items = us.get_preference_unregistered_items(userId)
        selected_items = random.sample(items, 6)
        # response = UserRepository.find_by_id(userId)
        response = items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response.model_dump_json())