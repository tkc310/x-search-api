from fastapi import FastAPI
from pydantic import BaseModel
from twikit import Client
from operator import itemgetter

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Body(BaseModel):
    uid: str
    email: str
    password: str
    target_uid: str

client = Client('ja-JP')
LIMIT_COUNT = 300

@app.post("/user_tweets")
async def list_user_tweet(body: Body, limit: int = LIMIT_COUNT):
    await client.login(
        auth_info_1=body.uid,
        auth_info_2=body.email,
        password=body.password
    )

    tweets = []
    try:
        # 最新300件のツイートを取得
        tweets = await client.search_tweet(
            query=f"from:{body.target_uid}",
            product='Latest',
            count=(LIMIT_COUNT if limit >= LIMIT_COUNT else limit)
        )
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return

    result = [{
        "id": tweet.id,
        "text": tweet.text,
        "view_count": int(tweet.view_count or 0),
        "created_at": tweet.created_at_datetime.strftime('%Y/%m/%d %H:%M:%S')
    } for tweet in tweets]

    return {
        "result": result
    }
