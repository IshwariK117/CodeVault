from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate, ProblemRead, ProblemUpdate

router = APIRouter()


@router.post("/", response_model=ProblemRead, status_code=status.HTTP_201_CREATED)
def create_problem(problem: ProblemCreate, db: Session = Depends(get_db)):
    db_problem = Problem(**problem.model_dump())
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem


@router.get("/", response_model=list[ProblemRead])
def list_problems(db: Session = Depends(get_db)):
    return db.query(Problem).order_by(Problem.id).all()


@router.get("/{problem_id}", response_model=ProblemRead)
def get_problem(problem_id: int, db: Session = Depends(get_db)):
    problem = db.get(Problem, problem_id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )
    return problem


@router.put("/{problem_id}", response_model=ProblemRead)
def update_problem(
    problem_id: int,
    problem_update: ProblemUpdate,
    db: Session = Depends(get_db),
):
    problem = db.get(Problem, problem_id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    update_data = problem_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(problem, field, value)

    db.commit()
    db.refresh(problem)
    return problem


@router.delete("/{problem_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_problem(problem_id: int, db: Session = Depends(get_db)):
    problem = db.get(Problem, problem_id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    db.delete(problem)
    db.commit()
