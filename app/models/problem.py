from datetime import date

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Problem(BaseModel):
    __tablename__ = "problems"

    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    platform: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    difficulty: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    language: Mapped[str] = mapped_column(String(50), nullable=False)
    approach: Mapped[str | None] = mapped_column(String(500), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    time_taken_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    complexity: Mapped[str | None] = mapped_column(String(100), nullable=True)
    solved_date: Mapped[date | None] = mapped_column(Date, nullable=True)
