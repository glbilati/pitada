from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class Health(BaseModel):
    status: str


@router.get("/healthz", response_model=Health)
def healthz() -> Health:
    # Liveness: nao toca no banco, para o Cloud Run nao reiniciar o container por falha do Neon.
    return Health(status="ok")
