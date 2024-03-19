from pydantic import BaseModel, UUID4
from domain import User, Category
from data.redis import RedisClient


class UserRepository(BaseModel):
    user: User

    def save(self):
        r = RedisClient()
        r.redis.set(str(self.user.id) + ":name", self.user.name)
        if self.user.selected_category is not None:
            for category in self.user.selected_category:
                r.redis.sadd(str(self.user.id) + ":selected_category", category.name)
        if self.user.preferences is not None:
            for item, like in self.user.preferences:
                r.redis.sadd(str(self.user.id) + ":preferences", item, like)
        if self.user.recommended_items is not None:
            for item in self.user.recommended_items:
                r.redis.rpush(str(self.user.id) + ":recommended_items", item)

    def update(self):
        # 一旦全て削除してから再登録
        self.delete()
        self.save()

    def delete(self):
        r = RedisClient()
        r.redis.delete(str(self.user.id) + ":name")
        r.redis.delete(str(self.user.id) + ":selected_category")
        r.redis.delete(str(self.user.id) + ":preferences")
        r.redis.delete(str(self.user.id) + ":recommended_items")

    @staticmethod
    def find_by_id(user_id: UUID4) -> User:
        r = RedisClient()
        name = r.redis.get(str(user_id) + ":name")
        selected_category_value = r.redis.smembers(str(user_id) + ":selected_category")
        selected_category = set([Category.create_by_name(value.decode('utf-8')) for value in selected_category_value])
        preferences = r.redis.smembers(str(user_id) + ":preferences")
        recommended_items = r.redis.lrange(str(user_id) + ":recommended_items", 0, -1)
        if name is None:
            return None
        user = User(
            id=user_id,
            name=name,
            selected_category=selected_category,
            preferences=preferences,
            recommended_items=recommended_items
        )
        return user
