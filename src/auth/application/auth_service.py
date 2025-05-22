import random
import string

import pendulum
from kink import inject

from src.auth.application.dto import BearerTokenDTO
from src.auth.domain.auth_repository import IAuthRepository


@inject
class AuthService:
    def __init__(self, auth_repo: IAuthRepository) -> None:
        self._auth_repo = auth_repo

    """Check if provided token is valid (exists and is not expired)

    Args:
        token (str): Bearer token to be checked.

    Returns:
        BearerTokenDTO object with the provided token and valid param
            if the token is expired or not.
    """

    def check(self, token: str) -> BearerTokenDTO:
        return BearerTokenDTO(
            token=token,
            valid=not self._auth_repo.get_bearer_token(token).is_expired(),
        )

    def generate_auth(self, expire_in: int) -> str:
        token = "".join(
            random.choices(
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits,
                k=32,
            )
        )
        exp_date = pendulum.now().add(days=expire_in)
        self._auth_repo.new_bearer_token(token=token, exp_date=exp_date)
        return token
