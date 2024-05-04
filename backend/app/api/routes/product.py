from fastapi import APIRouter

from backend.app.crud.product import get_product_type_by_id, get_all_product_types
from backend.app.api.dependencies.core import Session
from backend.app.schemas.product import ProductType
router = APIRouter(prefix="/api")


@router.get("/product-types/{id}/", response_model=ProductType)
async def retrieve_product_type(id: int, db: Session):
    return await get_product_type_by_id(id=id, db=db)


@router.get("/product-types/", response_model=list[ProductType])
async def get_product_types(db: Session):
    return await get_all_product_types(db=db)
