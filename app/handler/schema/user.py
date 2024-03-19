from pydantic import BaseModel, UUID4


class UserCreateModel(BaseModel):
    name: str


class UserCreateResponseModel(BaseModel):
    id: UUID4
    name: str
