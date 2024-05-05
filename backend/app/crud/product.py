from fastapi import HTTPException, Response
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette import status

from backend.app.models.product import ProductType
from backend.app.schemas.product import ProductTypeCreate


async def get_product_type_by_id(db: AsyncSession, id: int) -> ProductType:
    product_type = (await db.scalars(select(ProductType).where(ProductType.id == id))).first()
    if not product_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product type not found")
    return product_type


async def get_all_product_types(db: AsyncSession) -> list[ProductType]:
    return (await db.scalars(select(ProductType))).all()


async def delete_product_type(db: AsyncSession, id: int) -> Response:
    product_type = (await db.scalars(select(ProductType).where(ProductType.id == id))).first()
    if not product_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product type not found")
    await db.execute(delete(ProductType).where(ProductType.id == id))
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def create_product_type(db: AsyncSession, product_type: ProductTypeCreate):
    if (await db.scalars(select(ProductType).where(ProductType.title == product_type.title))).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product with this title already exists")

    db_product_type = ProductType(title=product_type.title, description=product_type.description)
    db.add(db_product_type)
    await db.commit()
    await db.refresh(db_product_type)
    return db_product_type
