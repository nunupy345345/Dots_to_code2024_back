import csv
from app.domain import Category, Item


def read_google_form_csv(path: str) -> list[Item]:
    """Googleフォームのデータを商品データに変換する
    Args:
        path (str): フォームのtsvファイルのパス
    Returns:
        list[Item]: 商品データのリスト
    """
    # 評価の変換辞書
    eval_dict = {
        "全く当てはまらない": 1,
        "当てはまらない": 2,
        "どちらとも言えない": 3,
        "当てはまる": 4,
        "とても良く当てはまる": 5
    }

    items = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # ヘッダー行を飛ばす
    for i, row in enumerate(reader):
        # 評価の変換
        evaluations = row[6:25]
        converted_evaluations = [eval_dict.get(eval_str, eval_str) for eval_str in evaluations]

        # 商品データに変換
        item = Item(
            id=i + 1,
            name=row[1],
            url=row[2],
            price=int(row[4]),
            category=Category(row[5]),
            image_url=row[3],
            evaluations=converted_evaluations
        )
        items.append(item)

    return items
