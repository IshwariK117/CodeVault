import json
from typing import Any

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


class ResponseFormatMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if should_skip_response_format(request, response):
            return response

        body = b""
        async for chunk in response.body_iterator:
            body += chunk

        try:
            payload = json.loads(body.decode())
        except json.JSONDecodeError:
            return rebuild_response(response, body)

        if is_already_formatted(payload):
            return rebuild_response(response, body)

        success = 200 <= response.status_code < 400
        formatted_payload = {
            "success": success,
            "status_code": response.status_code,
            "message": get_response_message(success, payload),
            "data": payload if success else None,
            "error": None if success else payload,
        }

        headers = dict(response.headers)
        headers.pop("content-length", None)

        return JSONResponse(
            content=formatted_payload,
            status_code=response.status_code,
            headers=headers,
            background=response.background,
        )


def should_skip_response_format(request: Request, response: Response) -> bool:
    content_type = response.headers.get("content-type", "")

    return (
        not request.url.path.startswith("/api")
        or response.status_code == 204
        or "application/json" not in content_type
    )


def is_already_formatted(payload: Any) -> bool:
    if not isinstance(payload, dict):
        return False

    return {"success", "status_code", "message", "data", "error"}.issubset(
        payload.keys()
    )


def get_response_message(success: bool, payload: Any) -> str:
    if success:
        return "Request successful"

    if isinstance(payload, dict) and isinstance(payload.get("detail"), str):
        return payload["detail"]

    return "Request failed"


def rebuild_response(response: Response, body: bytes) -> Response:
    headers = dict(response.headers)
    headers.pop("content-length", None)

    return Response(
        content=body,
        status_code=response.status_code,
        headers=headers,
        media_type=response.media_type,
        background=response.background,
    )
