from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)

from .config import get_settings


ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def verify_password(
    password: str,
    password_hash: str,
) -> bool:
    return check_password_hash(
        password_hash,
        password,
    )


def create_access_token(user_id: int) -> str:
    settings = get_settings()

    expire = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=settings.access_token_expire_minutes
        )
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> int | None:

    try:
        payload = jwt.decode(
            token,
            get_settings().secret_key,
            algorithms=[ALGORITHM],
        )

        return int(payload["sub"])

    except (
        JWTError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return None