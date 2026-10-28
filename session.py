"""Small synthetic session-expiration fixture; no credentials or real users."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    user_id: str
    issued_at: int
    ttl_seconds: int


def session_is_valid(session: Session, now: int) -> bool:
    """A session must be invalid at its expiration deadline."""
    expires_at = session.issued_at + session.ttl_seconds
    return now < expires_at


def get_current_user(session: Session, now: int) -> str | None:
    if session_is_valid(session, now):
        return session.user_id
    return None
