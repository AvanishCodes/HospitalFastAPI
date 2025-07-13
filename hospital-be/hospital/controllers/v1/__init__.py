from fastapi.routing import APIRouter
from .hospital import router as hospital_router

router = APIRouter()

router.include_router(hospital_router, prefix="/hospital", tags=["v1/hospital"])

__all__ = ["router"]
