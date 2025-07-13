from fastapi import FastAPI
from dotenv import load_dotenv

from .controllers import health_router, v1_router

load_dotenv()

app = FastAPI()

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(v1_router, prefix="/api/v1", tags=["v1"])
