from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def family():
    return {"father": "son"}

app.get("/job")
def getJobs(): 
    return [{
        "id": "uid1",
        "title": "Nice job",
        "description": "super nice job"
    },{
        "id": "uid2",
        "title": "Best Job",
        "description": "super working environment"
    }]