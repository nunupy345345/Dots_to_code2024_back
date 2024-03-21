from data.item import read_google_form_tsv
from domain import Item, Category

_all_items = read_google_form_tsv("./data/item_form.tsv")
_all_items_dict = {item.id: item for item in _all_items}
_all_categories = {item.category for item in _all_items}
_all_items_by_category_dict = {
    category.name: [item for item in _all_items if item.category.name == category.name] for category
    in
    _all_categories}


class ItemService:
    @staticmethod
    def get_all_items() -> list[Item]:
        return _all_items

    @staticmethod
    def get_item_by_id(item_id: int) -> Item:
        return _all_items_dict[item_id]

    @staticmethod
    def get_category_items_by_category(category: Category) -> list[Item]:
        return _all_items_by_category_dict[category.name]
