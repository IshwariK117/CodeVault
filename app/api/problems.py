from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_problems():
    return {"message": "Problems endpoint is ready"}
