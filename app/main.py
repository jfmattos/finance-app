from fastapi import FastAPI
from app.routers import health

# creating the app FastAPI
app = FastAPI()

# linking health router 
app.include_router(health.router)


# endpoint to test the root
@app.get("/")
def status():
    return {"yeah": "it's working"}
