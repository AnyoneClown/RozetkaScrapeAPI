from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import TIMESTAMP, Column

from backend.app.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
