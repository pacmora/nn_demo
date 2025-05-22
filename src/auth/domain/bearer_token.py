import pendulum


class BearerToken:
    """This class represent a Bearer token

    Args:
        token (str): Bearer token value, if it is not provided
            an exception will be raised

        creation_date (pendulum): Optional parameter,
            if it is not provided will take the current time

        exp_date (pendulum): Optional parameter, if date is not provided,
            expiration date will be 30 days in the future based on
            creation_date param
    """

    def __init__(
        self,
        token: str,
        creation_date: pendulum = pendulum.now("UTC"),
        exp_date: pendulum = None,
    ):

        if not token:
            raise ValueError("Token param cannot be empty")

        self._token = token
        self._creation_date = creation_date
        if exp_date is None:
            self._exp_date = self._creation_date.add(days=30)
        else:
            self._exp_date = exp_date

    """Check if this bearer token is already expired comparing
    current time and exp_date

    Returns:
        bool: True when current time is bigger than exp_date.
        In other cases returns False
    """

    def is_expired(self) -> bool:
        return pendulum.now("UTC") > self._exp_date
