from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home() -> HTMLResponse:
    html_file = Path(__file__).resolve().parents[1] / "static" / "index.html"
    return HTMLResponse(content=html_file.read_text(encoding="utf-8"))
