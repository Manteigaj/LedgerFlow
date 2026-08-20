from fastapi import FastAPI
from app.routes.upload import router
from app.routes.auth_routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(router)
