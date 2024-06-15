from typing import Annotated

import jwt
from fastapi import HTTPException, Depends
from jwt import InvalidTokenError
from sqlalchemy import select
from starlette import status

from backend.app.api.dependencies.core import Session, oauth2_scheme
from backend.app.models.user import User
from backend.app.schemas.user import TokenData, UserInDb, UserOut
from backend.app.utils import JWT_SECRET_KEY, ALGORITHM, get_hashed_password


async def get_user(db: Session, email: str):
    user = (await db.scalars(select(User).where(User.email == email))).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(db=db, email=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def create_user(data: UserInDb, db: Session):
    user = (await db.scalars(select(User).where(User.email == data.email))).first()
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = User(email=data.email, password=get_hashed_password(data.password), active=False)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserOut(id=user.id, email=user.email, active=user.active, created_at=user.created_at)
