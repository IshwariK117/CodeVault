from datetime import datetime
from uuid import UUID as PythonUUID
from uuid import uuid4

from sqlalchemy import DateTime, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uuid: Mapped[PythonUUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid4,
        unique=True,
        index=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
