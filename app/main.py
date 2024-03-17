import uvicorn
from fastapi import FastAPI
# COMMENT: ↓CORSを有効にしたいとき使う
# from fastapi_cors import CORS 
from model import TagModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/recomend")
async def(tag: TagModel)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)