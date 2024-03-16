import uvicorn
from fastapi import FastAPI

# MEMO ↓CORSを有効にしたいとき使う
# from fastapi_cors import CORS 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
