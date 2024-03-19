from domain import Category


class CategoryService:
    @staticmethod
    def get_all():
        return Category.get_all_categories()
