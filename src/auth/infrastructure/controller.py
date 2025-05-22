import typing as t

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from kink import di

from src.auth.application.auth_service import AuthService
from src.auth.application.dto import BearerTokenDTO
from src.auth.domain.auth_repository import IAuthRepository
from src.auth.infrastructure.in_memory_auth_repository import (
    InMemoryAuthRepository,
)
from src.building_blocks.errors import APIErrorMessage

repository = InMemoryAuthRepository()

di[IAuthRepository] = repository
di[AuthService] = AuthService(auth_repo=repository)

router = APIRouter()


async def validate_token(
    auth: t.Optional[HTTPAuthorizationCredentials] = Depends(
        HTTPBearer(auto_error=False)
    ),
    service: AuthService = Depends(lambda: di[AuthService]),
) -> str:
    token = service.check(auth.credentials)

    if not token.valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer token invalid or expired",
        )
    return auth.credentials


@router.get(
    "/auth",
    response_model=BearerTokenDTO,
    responses={
        400: {"model": APIErrorMessage},
        401: {"model": APIErrorMessage},
        500: {"model": APIErrorMessage},
    },
    tags=["Bearer token verification"],
    description="Verify if you bearer token is valid or not.",
)
async def auth_verification(
    token: BearerTokenDTO = Depends(validate_token),
    service: AuthService = Depends(lambda: di[AuthService]),
) -> JSONResponse:
    result = service.check(token)
    return JSONResponse(content=result.dict(), status_code=status.HTTP_200_OK)
