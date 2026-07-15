from fastapi import APIRouter, HTTPException, status

from app.schemas.problem import ProblemCreate, ProblemRead, ProblemUpdate

router = APIRouter()

problems: list[ProblemRead] = []
next_problem_id = 1


@router.post("/", response_model=ProblemRead, status_code=status.HTTP_201_CREATED)
def create_problem(problem: ProblemCreate):
    global next_problem_id

    new_problem = ProblemRead(id=next_problem_id, **problem.model_dump())
    problems.append(new_problem)
    next_problem_id += 1
    return new_problem


@router.get("/", response_model=list[ProblemRead])
def list_problems():
    return problems


@router.get("/{problem_id}", response_model=ProblemRead)
def get_problem(problem_id: int):
    problem = find_problem(problem_id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )
    return problem


@router.put("/{problem_id}", response_model=ProblemRead)
def update_problem(problem_id: int, problem_update: ProblemUpdate):
    problem = find_problem(problem_id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    update_data = problem_update.model_dump(exclude_unset=True)
    updated_problem = problem.model_copy(update=update_data)

    problem_index = problems.index(problem)
    problems[problem_index] = updated_problem
    return updated_problem


@router.delete("/{problem_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_problem(problem_id: int):
    problem = find_problem(problem_id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    problems.remove(problem)


def find_problem(problem_id: int):
    return next((problem for problem in problems if problem.id == problem_id), None)
