import unittest
from domain import Category
from services.user import UserService
from services.item import ItemService
from repository.user import UserRepository


class TestUserService(unittest.TestCase):
    def test_create_user(self):
        us = UserService()
        user = us.create_user_and_save("test_user")
        self.assertEqual(user.name, "test_user")
        registered_user = UserRepository.find_by_id(user.id)
        self.assertEqual(registered_user.name, "test_user")

    def test_register_item_category(self):
        us = UserService()
        user = us.create_user_and_save("test_user_test_register_item_category")
        # カテゴリを登録
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        # カテゴリが登録されているか確認
        registered_user = UserRepository.find_by_id(user.id)
        self.assertNotEqual(registered_user.selected_category, None)
        self.assertIn(Category.cosme_beauty, registered_user.selected_category)

    def test_register_user_preferences(self):
        us = UserService()
        user = us.create_user_and_save("test_user_test_register_user_preferences")
        registered_user_1 = UserRepository.find_by_id(user.id)
        # ユーザーの好みを登録
        self.assertEqual(registered_user_1.preferences, {})
        item1 = ItemService.get_all_items()[0]
        item2 = ItemService.get_all_items()[1]
        us.register_user_preferences(user.id, [(item1, True), (item2, False)])
        # 好みが登録されているか確認
        registered_user_2 = UserRepository.find_by_id(user.id)
        self.assertNotEqual(registered_user_2.preferences, None)
        self.assertIn(2, registered_user_2.preferences)
        self.assertIn(1, registered_user_2.preferences)

    def test_get_preference_unregistered_items(self):
        us = UserService()
        user = us.create_user_and_save("test_user_test_get_preference_unregistered_items")
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        user2 = UserRepository.find_by_id(user.id)
        self.assertEqual(user2.selected_category, {Category.cosme_beauty})
        # 未登録の商品を取得
        items = us.get_preference_unregistered_items(user.id)
        self.assertNotEqual(items, None)
        for item in items:
            self.assertEqual(Category.cosme_beauty, item.category)
        self.assertEqual(len(items), 5)  # google formのデータが変わり次第変わる


if __name__ == '__main__':
    unittest.main()
