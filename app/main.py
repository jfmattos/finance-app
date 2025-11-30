from fastapi import FastAPI

#importing the routers and connecting to the app
from app.routers import health, dashboard, transactions

# creating the app FastAPI
app = FastAPI()

# linking the routers
app.include_router(health.router) #GET /health
app.include_router(dashboard.router) #GET /dashboard/summary
app.include_router(transactions.router) #GET /transactions

# endpoint to test the root
@app.get("/")
def status():
    return {"yeah": "it's working"}

#endpoint to test
@app.get("/hello")
def say_hello():
    # random route to test
    return {"message": "Hello, finance app!"}
