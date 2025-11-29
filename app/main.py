from fastapi import FastAPI

# creating the app FastAPI
app = FastAPI()

# endpoint to test the root
@app.get("/")
def status():
    return {"yeah": "it's working"}

# endpoint to test the api
@app.get("/health")
def health_check():
    return {"status": "ok"}
