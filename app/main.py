from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import get_settings
from .database import init_db
from .services.gemini_service import gemini_service

from .routers import (
    auth,
    pages,
    recommendations,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


settings = get_settings()


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)


app.include_router(
    pages.router
)

app.include_router(
    auth.router
)

app.include_router(
    recommendations.router
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "gemini_configured": gemini_service.configured,
    }