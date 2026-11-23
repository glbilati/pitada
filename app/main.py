from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.errors import install_error_handlers
from app.modules.auth.router import router as auth_router
from app.modules.health.router import router as health_router

WEB_DIST = Path(__file__).resolve().parent.parent / "web" / "dist"


def create_app() -> FastAPI:
    app = FastAPI(title="Pitada", version="0.1.0")
    install_error_handlers(app)
    app.include_router(health_router)
    app.include_router(auth_router)
    # Mesma origem: o FastAPI serve o front estatico, sem CORS. Montado por ultimo para
    # nao esconder as rotas da API.
    if WEB_DIST.is_dir():
        app.mount("/", StaticFiles(directory=WEB_DIST, html=True), name="web")
    return app


app = create_app()
