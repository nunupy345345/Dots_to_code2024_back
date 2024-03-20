from pydantic import BaseModel


class PreferenceModel(BaseModel):
    itemId: int
    is_like: bool


class RegisterPreferencesModel(BaseModel):
    PreferenceList: list[PreferenceModel]
