from pydantic import BaseModel


class BearerTokenDTO(BaseModel):
    token: str
    valid: bool
