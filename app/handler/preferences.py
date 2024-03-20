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

        for preference in request_body.PreferenceList:
            item_id = preference.itemId
            item_detail = ItemService.get_all_items()[item_id-1]
            is_like = preference.is_like
            item_list.append((item_detail, is_like))
            
        # MEMO: test用
        us.register_user_preferences(user_id, item_list)
        user = UserRepository.find_by_id(user_id)
        
        # MEMO: test後 response = {"status":"Successful Operation"}にする
        response = user.preferences
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error create user: {str(e)}")
    return JSONResponse(status_code=200, content=response)
