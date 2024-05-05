from pydantic import BaseModel


class ProductTypeBase(BaseModel):
    title: str
    description: str | None = None


class ProductTypeCreate(ProductTypeBase):
    title: str
    description: str | None = None


class ProductType(ProductTypeBase):
    id: int

    class Config:
        from_attributes = True
