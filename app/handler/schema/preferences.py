from pydantic import BaseModel


class PreferenceModel(BaseModel):
    item_id: int
    is_like: bool


class RegisterPreferencesModel(BaseModel):
    preference_list: list[PreferenceModel]
