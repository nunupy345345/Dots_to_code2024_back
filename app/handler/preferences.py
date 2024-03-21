from .schema import RegisterPreferencesModel, PreferenceModel
from services.user import UserService
from services.item import ItemService
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import json
from repository.user import UserRepository

def register_preferences_handler(user_id: str, request_body:RegisterPreferencesModel):
    try:
        """
        ユーザーの各アイテムの好みを登録する
        """
        us = UserService()
        item_list = []

        for preference in request_body.preference_list:
            item_id = preference.item_id
            item_detail = ItemService.get_item_by_id(item_id)
            is_like = preference.is_like
            item_list.append((item_detail, is_like))

        response = {"status":"Successful Operation"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response)
