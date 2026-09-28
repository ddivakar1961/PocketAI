from __future__ import annotations

from app.config import get_settings


class GeminiService:
    def __init__(self) -> None:
        self.configured = bool(get_settings().gemini_api_key)


gemini_service = GeminiService()
