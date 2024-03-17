import numpy as np

from app.domain import Item


class ItemRecommend:
    def __init__(self, items):
        self.items: list[Item] = items
        self.item_vec: np.array = np.array([item.evaluations for item in items])
        self.similarities = self.calc_similarity()

    def calc_similarity(self) -> np.array:
        """
        アイテム同士のコサイン類似度行列を計算しておく
        """
        similarities = np.zeros((self.item_vec.shape[0], self.item_vec.shape[0]))

        for i1, v1 in enumerate(self.item_vec):
            for i2, v2 in enumerate(self.item_vec):
                if i1 == i2:
                    similarities[i1][i2] = np.nan
                else:
                    similarities[i1][i2] = np.dot(v1, v2.T) / (np.linalg.norm(v1) * np.linalg.norm(v2))

        return similarities

    def predict_rating(self, user_rating: dict, item_index) -> float:
        """ユーザーの評価値と商品の類似度を元に評価値を予測する

        Args:
            user_rating (np.array): ユーザーの評価値
            item_index (int): 商品のインデックス

        Returns:
            float: 予測された評価値
        """
        numerator = 0.0
        enumerator = 0.0

        for idx, rating in user_rating.items():
            numerator += self.similarities[item_index][idx] * rating
            enumerator += self.similarities[item_index][idx]

        return numerator / enumerator if enumerator != 0 else np.nan
