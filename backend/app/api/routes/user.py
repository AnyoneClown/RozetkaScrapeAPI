from fastapi import APIRouter

from backend.app.crud import user as user_crud
from backend.app.api.dependencies.core import Session
from backend.app.schemas.user import UserInDb

router = APIRouter()


@router.post("/signup/", summary="Create new user")
async def create_user(data: UserInDb, db: Session):
    return await user_crud.create_user(db=db, data=data)
