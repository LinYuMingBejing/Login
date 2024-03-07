from dataclasses import dataclass
from typing import Optional


@dataclass
class Response:
    success: bool
    reason: str
    payload: Optional[dict] = None


def success(reason=None, payload=None):
    return Response(success=True, reason=reason, payload=payload)


def error(reason=None):
    return Response(success=False, reason=reason)

