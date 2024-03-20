from repository.user import UserRepository
from services.item import ItemService
from pydantic import UUID4 as UUID4Type
from domain import User, Category, Item
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

    @staticmethod
    def get_preference_unregistered_items(user_id: UUID4Type) -> list[Item]:
        user = UserRepository.find_by_id(user_id)
        print(user)
        items_candidate = set()
        if user.selected_category is None:
            items_candidate = set([item.id for item in ItemService.get_all_items()])
        else:
            for category in user.selected_category:
                items_candidate |= {item.id for item in ItemService.get_category_items_by_category(category)}
        for item_id in user.preferences.keys():
            items_candidate.discard(item_id)
        return [ItemService.get_item_by_id(item_id) for item_id in items_candidate]
