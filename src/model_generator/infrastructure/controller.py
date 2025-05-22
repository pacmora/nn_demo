from fastapi import APIRouter, Depends, status
from kink import di

from src.auth.application.auth_service import AuthService
from src.auth.application.dto import BearerTokenDTO
from src.auth.domain.auth_repository import IAuthRepository
from src.auth.infrastructure.controller import validate_token
from src.auth.infrastructure.in_memory_auth_repository import (
    InMemoryAuthRepository,
)
from src.building_blocks.errors import APIErrorMessage
from src.model_generator.application.dto import ModelDTO
from src.model_generator.application.model_service import ModelService
from src.model_generator.domain.model import Model
from src.model_generator.infrastructure.yaml_response import YAMLResponse

repository = InMemoryAuthRepository()

di[IAuthRepository] = repository
di[AuthService] = AuthService(auth_repo=repository)
di[ModelService] = ModelService()

router = APIRouter()

# Model object as example only for /docs
model_example: Model = Model(
    name="Your model name",
    url="URL where model is stored",
    replicas=2,
    memory="250Ki",
)


@router.post(
    "/model",
    response_model=ModelDTO,
    response_class=YAMLResponse,
    responses={
        200: {
            "content": {
                "text/yaml": {"example": model_example.model_to_dict()}
            },
            "description": "Return YAML model",
        },
        400: {
            "model": APIErrorMessage,
            "content": {
                "application/json": {
                    "example": {"type": "string", "message": "string"}
                }
            },
        },
        404: {
            "model": APIErrorMessage,
            "content": {
                "application/json": {
                    "example": {"type": "string", "message": "string"}
                }
            },
        },
        422: {
            "model": APIErrorMessage,
            "content": {
                "application/json": {
                    "example": {"type": "string", "message": "string"}
                }
            },
        },
        500: {
            "model": APIErrorMessage,
            "content": {
                "application/json": {
                    "example": {"type": "string", "message": "string"}
                }
            },
        },
    },
    tags=["Generate model yaml"],
    description="Provide params to generate yaml model.",
)
async def generate_model(
    model: Model,
    token: BearerTokenDTO = Depends(validate_token),
    service: ModelService = Depends(lambda: di[ModelService]),
) -> YAMLResponse:
    response = service.generate_model(model)
    return YAMLResponse(
        content=response,
        media_type="text/yaml",
        status_code=status.HTTP_200_OK,
    )
