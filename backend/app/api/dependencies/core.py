from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database import sessionmanager


async def get_db_session():
    async with sessionmanager.session() as session:
        yield session

Session = Annotated[AsyncSession, Depends(get_db_session)]
