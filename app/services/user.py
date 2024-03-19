from repository.user import UserRepository
from pydantic import UUID4 as UUID4Type
from domain.user import User
from uuid import uuid4


class UserService:
    @staticmethod
    def register_item_category(user_id: UUID4Type, category_list: list[str]) -> None:
        user_repository = UserRepository()
        user = user_repository.find_by_id(user_id)
        categories = [Category.create_by_name(category) for category in category_list]
        user.selected_category = categories
        UserRepository(user).save()  # 上書き更新

    @staticmethod
    def create_user(name: str):
        uuid = uuid4()
        user = User(id=uuid, name=name)
        ur = UserRepository(user=user)
        try:
            ur.save()
        except Exception as e:
            raise Exception(f"{__file__}: {str(e)}")
        return user
