from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class ProblemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    platform: str = Field(..., min_length=1, max_length=100)
    difficulty: str = Field(..., min_length=1, max_length=50)
    status: str = Field(..., min_length=1, max_length=50)
    language: str = Field(..., min_length=1, max_length=50)
    approach: str | None = Field(default=None, max_length=500)
    notes: str | None = None
    time_taken_minutes: int | None = Field(default=None, ge=0)
    complexity: str | None = Field(default=None, max_length=100)
    solved_date: date | None = None


class ProblemCreate(ProblemBase):
    pass


class ProblemUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    platform: str | None = Field(default=None, min_length=1, max_length=100)
    difficulty: str | None = Field(default=None, min_length=1, max_length=50)
    status: str | None = Field(default=None, min_length=1, max_length=50)
    language: str | None = Field(default=None, min_length=1, max_length=50)
    approach: str | None = Field(default=None, max_length=500)
    notes: str | None = None
    time_taken_minutes: int | None = Field(default=None, ge=0)
    complexity: str | None = Field(default=None, max_length=100)
    solved_date: date | None = None


class ProblemRead(ProblemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
