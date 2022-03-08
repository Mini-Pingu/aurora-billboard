from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/tasks",
    tags=["items"],
    responses={404: {"description": "Not found"}}
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_tasks():
    return fake_items_db
