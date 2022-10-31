from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def family():
    return {"father": "son"}