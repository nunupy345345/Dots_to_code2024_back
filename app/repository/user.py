from pydantic import BaseModel, UUID4
from domain import Category, User
from data.redis import RedisClient
from services.item import ItemService


class UserRepository(BaseModel):

    @classmethod
    def save(cls, user: User):
        r = RedisClient()
        r.redis.set(str(user.id) + ":name", user.name)
        if user.selected_category is not None:
            for category in user.selected_category:
                try:
                    r.redis.sadd(str(user.id) + ":selected_category", category.name)
                except Exception as e:
                    raise Exception(f"{__file__}: {str(e)}")
        if user.preferences is not None:
            for itemId, like in user.preferences.items():
                r.redis.hset(str(user.id) + ":preferences", itemId, int(like))
        if user.recommended_items is not None:
            for item in user.recommended_items:
                r.redis.rpush(str(user.id) + ":recommended_items", item.id)

    @classmethod
    def update(cls, user: User):
        # 一旦全て削除してから再登録
        cls.delete(user)
        cls.save(user)

    @classmethod
    def delete(cls, user: User):
        r = RedisClient()
        r.redis.delete(str(user.id) + ":name")
        r.redis.delete(str(user.id) + ":selected_category")
        r.redis.delete(str(user.id) + ":preferences")
        r.redis.delete(str(user.id) + ":recommended_items")

    @staticmethod
    def find_by_id(user_id: UUID4) -> User:
        r = RedisClient()
        name = r.redis.get(str(user_id) + ":name")
        selected_category_value = r.redis.smembers(str(user_id) + ":selected_category")
        selected_category = set([Category.create_by_name(value.decode('utf-8')) for value in selected_category_value])
        preferences = r.redis.hgetall(str(user_id) + ":preferences")
        recommended_items_id = r.redis.lrange(str(user_id) + ":recommended_items", 0, -1)
        recommended_items = []
        for item_id in recommended_items_id:
            decoded_item_id: str = item_id.decode("utf-8")
            recommended_items.append(ItemService.get_item_by_id(int(decoded_item_id)))
        if name is None:
            return None
        new_preferences = {}
        for key, value in preferences.items():
            new_preferences[key.decode("utf-8")] = bool(int(value.decode("utf-8")))
        user = User(
            id=user_id,
            name=name,
            selected_category=selected_category,
            preferences=new_preferences,
            recommended_items=recommended_items
        )
        return user
