from fastapi import APIRouter

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/health")
def recommendations_health() -> dict[str, str]:
    return {"status": "ok"}
