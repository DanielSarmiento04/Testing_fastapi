from ..models.Item import Item
from ..dependencies import oauth2_scheme
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme)],
)

@router.get("/")
def init():
    return {"module": "users"}

@router.get("/{id}/name")
async def read_item_name(id: int):
    return {"item_id": id, "name": "Foo Bar"}

@router.get("/items/")
async def get_items(token:str = Depends(oauth2_scheme)):
    return {"token": token}


