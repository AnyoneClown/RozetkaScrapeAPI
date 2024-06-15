from fastapi import APIRouter

from backend.app.api.dependencies.core import Session
from backend.app.crud.product import (
    create_product_type,
    delete_product_type,
    get_all_product_types,
    get_product_type_by_id,
)
from backend.app.schemas.product import ProductType, ProductTypeCreate

router = APIRouter()


@router.get("/product-types/{id}/", response_model=ProductType)
async def retrieve_product_types(id: int, db: Session):
    return await get_product_type_by_id(id=id, db=db)


@router.get("/product-types/", response_model=list[ProductType])
async def get_product_types(db: Session):
    return await get_all_product_types(db=db)


@router.delete("/product-types/{id}/", response_model=ProductType)
async def delete_product_types(id: int, db: Session):
    return await delete_product_type(id=id, db=db)


@router.post("/product-types/", response_model=ProductType)
async def post_product_type(db: Session, product_type: ProductTypeCreate):
    return await create_product_type(db=db, product_type=product_type)
