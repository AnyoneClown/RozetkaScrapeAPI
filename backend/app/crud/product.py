from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.app.models.product import ProductType


async def get_product_type_by_id(db: AsyncSession, id: int) -> ProductType:
    result = await db.execute(select(ProductType).where(ProductType.id == id))
    product_type = result.scalars().first()
    if not product_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product type not found")
    return product_type


async def get_all_product_types(db: AsyncSession) -> [ProductType]:
    result = await db.execute(select(ProductType))
    return result.scalars().all()
