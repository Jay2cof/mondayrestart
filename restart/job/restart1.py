from fastapi import FastAPI, HTTPException

app = FastAPI()

Jobs_data= [{
        "id": "uid1",
        "title": "Nice job1",
        "description": "super nice job"
}, {
        "id": "uid2",
        "title": "Nice Job2",
        "description": "super nice job2"
}]


@app.get("/")
def family():
    return {"father": "son"}


@app.get("/job")
def getJobs(): 
    return Jobs_data


@app.get("/job/{id}")
def getJobs(id): 
    for job in Jobs_data:
        if (job["id"] == id):
            return job
    raise HTTPException(
        status_code=404, detail="Job with id " + id + " not found")


    

