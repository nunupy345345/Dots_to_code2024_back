import unittest
from domain import User, Category
from services.user import UserService
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
        self.assertEqual(registered_user_1.preferences, None)
        us.register_user_preferences(user.id, [(Category.cosme_beauty, True), (Category.food_sweet, False)])
        # 好みが登録されているか確認
        registered_user_2 = UserRepository.find_by_id(user.id)
        self.assertNotEqual(registered_user_2.preferences, None)
        self.assertIn(Category.cosme_beauty, registered_user_2.preferences)
        self.assertIn(Category.food_sweet, registered_user_2.preferences)


if __name__ == '__main__':
    unittest.main()
