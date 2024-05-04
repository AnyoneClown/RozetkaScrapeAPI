from pydantic import BaseModel


class ProductTypeBase(BaseModel):
    title: str
    description: str | None = None


class ProductTypeCreate(ProductTypeBase):
    pass


class ProductTypeDelete(ProductTypeBase):
    id: int


class ProductType(ProductTypeBase):
    id: int

    class Config:
        from_attributes = True
