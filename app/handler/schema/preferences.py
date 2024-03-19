from pydantic import BaseModel, UUID4


class RegisterPreferencesModel(BaseModel):
    userId: UUID4
    PreferenceList: list[PreferenceModel]
    
class PreferenceModel(BaseModel):
    itemId: UUID4
    is_like: bool
