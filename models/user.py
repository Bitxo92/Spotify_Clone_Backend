from models.base import Base
from sqlalchemy import UUID, VARCHAR, Column, LargeBinary
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100), unique=True)
    password = Column(LargeBinary(100))