"""Contrato de login da F0. Os handlers ainda respondem 501: implementar e o trabalho da F0."""

from fastapi import APIRouter, Response

from app.errors import PROBLEM_JSON, Problem, problem_response
from app.modules.auth.schemas import LoginRequest, UserOut

router = APIRouter(prefix="/api/v1", tags=["auth"])

_problem = {"model": Problem, "content": {PROBLEM_JSON: {}}}


def _not_implemented() -> Response:
    return problem_response(501, "Nao implementado")


@router.post(
    "/auth/login",
    response_model=UserOut,
    responses={401: {**_problem, "description": "Credenciais invalidas"}, 501: _problem},
)
def login(body: LoginRequest) -> Response:
    return _not_implemented()


@router.post("/auth/logout", status_code=204, responses={501: _problem})
def logout() -> Response:
    return _not_implemented()


@router.get(
    "/me",
    response_model=UserOut,
    responses={401: {**_problem, "description": "Sem sessao"}, 501: _problem},
)
def me() -> Response:
    return _not_implemented()
