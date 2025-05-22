from abc import ABC, abstractmethod

from pendulum import datetime

from src.auth.domain.bearer_token import BearerToken


class IAuthRepository(ABC):

    @abstractmethod
    def get_bearer_token(self, token: str) -> BearerToken:
        pass

    @abstractmethod
    def new_bearer_token(self, token: str, exp_date: datetime):
        pass
