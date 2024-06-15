from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database import sessionmanager


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmanager.session() as session:
        yield session

Session = Annotated[AsyncSession, Depends(get_db_session)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
