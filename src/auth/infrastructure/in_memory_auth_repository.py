import pendulum

from src.auth.domain.auth_repository import IAuthRepository
from src.auth.domain.bearer_token import BearerToken


class InMemoryAuthRepository(IAuthRepository):

    def __init__(self):
        self._bearer_tokens = dict()
        self._bearer_tokens["uee580oNP3mo3WXwgmLU9CBaonYKsd2h"] = BearerToken(
            token="uee580oNP3mo3WXwgmLU9CBaonYKsd2h"
        )
        self._bearer_tokens["CMorqkUvwK7vbg0C03p80trWTZuKzrIz"] = BearerToken(
            token="CMorqkUvwK7vbg0C03p80trWTZuKzrIz",
            exp_date=pendulum.now("UTC").add(days=10),
        )
        self._bearer_tokens["m0KJtzarRaDZauzQWRyPLLo4G34CmOke"] = BearerToken(
            token="m0KJtzarRaDZauzQWRyPLLo4G34CmOke",
            exp_date=pendulum.now("UTC").add(days=11),
        )
        self._bearer_tokens["EaQ08LzPfc0Oke65ChGYe05lYy2CjnSt"] = BearerToken(
            token="EaQ08LzPfc0Oke65ChGYe05lYy2CjnSt",
            exp_date=pendulum.now("UTC").add(days=12),
        )
        self._bearer_tokens["1UdbPvnwqQjOdP9wBh7iO3l8mdK6r4Jj"] = BearerToken(
            token="1UdbPvnwqQjOdP9wBh7iO3l8mdK6r4Jj",
            exp_date=pendulum.now("UTC").add(days=-10),
        )

    """ Retrieve a BearerToken from repository.

    Args:
        token (str): The token to be retrieved.

    Returns:
        If the token exists, even if it is expired, is returned from repository.
        If the token does not exist returns a fake token already expired
    """

    def get_bearer_token(self, token: str) -> BearerToken:
        if token in self._bearer_tokens:
            return self._bearer_tokens.get(token)
        else:
            return BearerToken(
                "no_token",
                creation_date=pendulum.datetime(1970, 1, 1, 0, 0, 0),
            )

    def new_bearer_token(self, token: str, exp_date: pendulum):
        self._bearer_tokens[token] = BearerToken(
            token=token, exp_date=exp_date
        )
