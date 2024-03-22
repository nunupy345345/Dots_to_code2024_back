from pydantic import BaseModel, UUID4


class UserCreateModel(BaseModel):
    name: str
    min_price: int
    max_price: int


class UserCreateResponseModel(BaseModel):
    id: UUID4
    name: str