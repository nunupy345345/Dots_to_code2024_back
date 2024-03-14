FROM python:3.11

# 文字、タイムゾーン設定
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt .

# PostgreSQLのランタイムライブラリとビルドに必要なパッケージをインストール
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql \
        libpq-dev \
        tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードを追加
COPY . /app

# FastAPIの起動
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]