import pytest as pytest

from src.auth.application.auth_service import AuthService
from src.auth.application.dto import BearerTokenDTO
from src.auth.infrastructure.in_memory_auth_repository import (
    InMemoryAuthRepository,
)


@pytest.fixture()
def auth_service() -> AuthService:
    repository = InMemoryAuthRepository()
    auth_service = AuthService(repository)
    return auth_service


def test_generate_auth(auth_service):
    token = auth_service.generate_auth(expire_in=10)
    assert len(token) == 32


def test_valid_auth(auth_service):
    token: BearerTokenDTO = auth_service.check(
        auth_service.generate_auth(expire_in=10)
    )
    assert token.valid


def test_expired_auth(auth_service):
    token_expired: BearerTokenDTO = auth_service.check(
        auth_service.generate_auth(expire_in=-10)
    )
    assert not token_expired.valid


def test_empty_token_auth(auth_service):
    token_empty: BearerTokenDTO = auth_service.check("")
    assert not token_empty.valid
