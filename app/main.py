from fastapi import FastAPI

from app.api.router import api_router
from app.middleware.response_format import ResponseFormatMiddleware

app = FastAPI()

app.add_middleware(ResponseFormatMiddleware)
app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
