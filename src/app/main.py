from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.get("/hello")
def hello():
    return {"hello": "hi!"}