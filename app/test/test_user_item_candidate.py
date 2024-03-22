import unittest
import sys
sys.path.append("./app")
from domain import Category
from services.user import UserService
from services.item import ItemService
from repository.user import UserRepository


class TestUserService(unittest.TestCase):
    def test_create_user(self):
        """
        ユーザーを作成するテスト
        """
        us = UserService()
        user = us.create_user_and_save("test_user",1000,10000)
        self.assertEqual(user.name, "test_user")
        self.assertEqual(user.min_price, 1000)
        self.assertEqual(user.max_price, 10000)
        registered_user = UserRepository.find_by_id(user.id)
        self.assertEqual(registered_user.name, "test_user")

    def test_create_user(self):
        """
        ユーザーを作成するテスト
        """
        us = UserService()
        user = us.create_user_and_save("test_user",1000,10000)
        self.assertEqual(user.name, "test_user")
        registered_user = UserRepository.find_by_id(user.id)
        self.assertEqual(registered_user.name, "test_user")
        
    def test_register_item_category(self):
        """
        ユーザーが選択したカテゴリを登録するテスト
        """
        us = UserService()
        user = us.create_user_and_save("test_user_test_register_item_category",1000,10000)
        # カテゴリを登録
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        # カテゴリが登録されているか確認
        registered_user = UserRepository.find_by_id(user.id)
        self.assertNotEqual(registered_user.selected_category, None)
        self.assertIn(Category.cosme_beauty, registered_user.selected_category)

    def test_register_user_preferences(self):
        """
        ユーザーの各アイテムの好みを登録するテスト
        """
        us = UserService()
        user = us.create_user_and_save("test_user_test_register_user_preferences",1000,10000)
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

    def test_get_preference_unregistered_items__no_preferences(self):
        """
        ユーザーの好みが登録されていない場合の未登録商品を取得するテスト
        """
        us = UserService()
        user = us.create_user_and_save("test_get_preference_unregistered_items__no_preferences",1000,10000)
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        user2 = UserRepository.find_by_id(user.id)
        self.assertEqual(user2.selected_category, {Category.cosme_beauty})
        # 未登録の商品を取得
        items = us.get_preference_unregistered_items(user.id)
        self.assertNotEqual(items, None)
        for item in items:
            self.assertEqual(Category.cosme_beauty, item.category)
        self.assertEqual(len(items), 5)  # google formのデータが変わり次第変わる

    def test_get_preference_unregistered_items__yes_preferences(self):
        """
        ユーザーの好みが登録されている場合の未登録商品を取得するテスト
        """
        us = UserService()
        user = us.create_user_and_save("test_get_preference_unregistered_items__yes_preferences",1000,10000)
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        cosme_items = ItemService.get_category_items_by_category(Category.cosme_beauty)
        us.register_user_preferences(user.id,
                                     [(cosme_items[0], True), (cosme_items[1], True)])
        user2 = UserRepository.find_by_id(user.id)
        self.assertEqual(user2.selected_category, {Category.cosme_beauty})
        # 未登録の商品を取得
        items = us.get_preference_unregistered_items(user.id)

        self.assertNotEqual(items, None)
        for item in items:
            self.assertEqual(Category.cosme_beauty, item.category)
        self.assertEqual(len(items), 3)

    def test_get_updated_user_recommend_items(self):
        us = UserService()
        user = us.create_user_and_save("test_get_updated_user_recommend_items",1000,10000)
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        cosme_items = ItemService.get_category_items_by_category(Category.cosme_beauty)
        us.register_user_preferences(user.id,
                                     [(cosme_items[0], True), (cosme_items[1], True)])
        recommended_items = us.get_updated_user_recommend_items(user.id)
        self.assertNotEqual(recommended_items, None)
        self.assertEqual(len(recommended_items), 5)

    def test_get_updated_user_recommend_items_second_time(self):
        us = UserService()
        user = us.create_user_and_save("test_get_updated_user_recommend_items_second_time",1000,10000)
        us.register_item_category(user.id, [Category.cosme_beauty.name])
        cosme_items = ItemService.get_category_items_by_category(Category.cosme_beauty)
        us.register_user_preferences(user.id,
                                     [(cosme_items[0], True), (cosme_items[1], True)])
        recommended_items = us.get_updated_user_recommend_items(user.id)
        self.assertNotEqual(recommended_items, None)
        self.assertEqual(len(recommended_items), 5)
        recommended_items = us.get_updated_user_recommend_items(user.id)
        self.assertNotEqual(recommended_items, None)
        self.assertEqual(len(recommended_items), 5)


if __name__ == '__main__':
    unittest.main()
