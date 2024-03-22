from repository.user import UserRepository
from services.item import ItemService
from pydantic import UUID4 as UUID4Type
from domain import User, Category, Item
from lib.recommend import ItemRecommend
from uuid import uuid4


class UserService:
    @staticmethod
    def register_item_category(user_id: UUID4Type, category_list: list[str]) -> None:
        user = UserRepository.find_by_id(user_id)
        categories = [Category.create_by_name(category) for category in category_list]
        user.selected_category = categories
        UserRepository.save(user)  # 上書き更新

    @staticmethod
    def create_user_and_save(name: str,min_price: int, max_price: int):
        uuid = uuid4()
        user = User.create(user_id=uuid, name=name, min_price=min_price, max_price=max_price)
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
        items_candidate = set()
        if user.selected_category is None:
            items_candidate = set([item.id for item in ItemService.get_all_items()])
        else:
            for category in user.selected_category:
                items_candidate |= {item.id for item in ItemService.get_category_items_by_category(category)}
        for item_id in user.preferences.keys():
            items_candidate.discard(item_id)
        return [ItemService.get_item_by_id(item_id) for item_id in items_candidate]

    @staticmethod
    def get_updated_user_recommend_items(user_id: UUID4Type) -> list[Item]:
        user = UserRepository.find_by_id(user_id)
        # おすすめの候補になるアイテムを取得
        # TODO: ここですでにユーザーに見せたアイテムを除外するのもあり（アイテム数が少ないから意味ないかも）
        item_candidate = set(ItemService.get_all_items())
        item_recommend = ItemRecommend(ItemService.get_all_items())
        ranking = []
        # おすすめのアイテムを計算
        for item_idx, item in enumerate(item_candidate):
            predict_rating = item_recommend.predict_rating(user.preferences, item_idx)
            ranking.append((item, predict_rating))

        # 評価値の高い順に並べ替え
        ranking = sorted(ranking, key=lambda x: x[1], reverse=True)

        # priceがmin_price未満、max_priceを超えるものはrankingから削除する
        min_price = user.min_price
        max_price = user.max_price
        ranking = [(item, rating) for item, rating in ranking if min_price <= item.price <= max_price]
        # ユーザーにおすすめのアイテムを登録
        user.recommended_items = [item for item, rating in ranking[:5]]
        UserRepository.save(user)
        return [item for item, rating in ranking[:5]]
