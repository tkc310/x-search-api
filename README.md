# x-search-api

twikitを利用して自分のアカウントでログインしてツイートを取得するAPI
公式の無料枠制限がきついため作成した

## Usage

```
# 開発環境に入ってパッケージインストール
$ pipenv shell
$ pipenv install

# 起動
$ pipenv run dev

# デプロイ
$ npx vercel login
$ npx vercel . # 初回のセットアップ・デプロイ
$ npx vercel --prod # 2回目以降のデプロイ
$ npx vercel dev # ローカル環境でのテスト
```

```
curl -X POST 'http://127.0.0.1:3001/user_tweets?limit=10' \
-H "Content-Type: application/json" \
-d '{"uid":"xxx", "email":"xxx", "password": "xxx", "target_uid": "xxx" }'
```
