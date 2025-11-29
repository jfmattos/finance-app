from fastapi import FastAPI
from app.routers import health, dashboard

# creating the app FastAPI
app = FastAPI()

# linking health and dashboard router
app.include_router(health.router)
app.include_router(dashboard.router)


# endpoint to test the root
@app.get("/")
def status():
    return {"yeah": "it's working"}
