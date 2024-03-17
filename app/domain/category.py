from enum import Enum

# MEMO category.nameで英語側を取り出す
class Category(Enum):
    cosme_beauty = "コスメ・ビューティー"
    food_sweet = "食品・スイーツ"
    fashion = "ファッション"
    accessory = "アクセサリー"
    interior = "インテリア"
    flower_plant = "花・植物"
    kitchen_table_ware = "キッチン・テーブルウェア"
    hobby_lifestyle_supplies = "趣味・ライフスタイル雑貨"
    others = "その他"
    
    @classmethod
    def create_by_name(cls, name: str):
        for category in Category:
            if category.name == name:
                return category
        raise ValueError(f'{name} は有効なカテゴリの値ではありません')
