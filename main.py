import uvicorn
from fastapi import FastAPI
from app.routers import expenses, categories, users
from app.routers.auth import login
app = FastAPI()
app.include_router(router=categories.router)
app.include_router(router=expenses.router)
app.include_router(router=login.router)
app.include_router(router=users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
