from repository.user import UserRepository
from pydantic import UUID4 as UUID4Type
from domain import User, Category
from uuid import uuid4


class UserService:
    @staticmethod
    def register_item_category(user_id: UUID4Type, category_list: list[str]) -> None:
        user = UserRepository.find_by_id(user_id)
        categories = [Category.create_by_name(category) for category in category_list]
        user.selected_category = categories
        UserRepository.save(user)  # 上書き更新

    @staticmethod
    def create_user_and_save(name: str):
        uuid = uuid4()
        user = User.create(user_id=uuid, name=name)
        try:
            UserRepository.save(user)
        except Exception as e:
            raise Exception(f"{__file__}: {str(e)}")
        return user

    @staticmethod
    def register_user_preferences(user_id: UUID4Type, item_list: list[tuple[Item, bool]]):
        user = UserRepository.find_by_id(user_id)
        preference_dict = {item.id: like for item, like in item_list}
        user.preferences.update(preference_dict)
        UserRepository.save(user)  # 上書き更新
