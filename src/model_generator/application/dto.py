from pydantic import BaseModel, Field


class ModelDTO(BaseModel):
    name: str = Field(min_length=3)
    url: str
    replicas: int = Field(gt=0)
    memory: str = Field(pattern=r"^\d+(Ei|Pi|Ti|Gi|Mi|Ki)$")
