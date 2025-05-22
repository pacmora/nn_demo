from pydantic import BaseModel, Field


class Model(BaseModel):
    name: str = Field(min_length=3)
    url: str
    replicas: int = Field(gt=0)
    memory: str = Field(pattern=r"^\d+(Ei|Pi|Ti|Gi|Mi|Ki)$")

    def model_to_dict(self) -> ():
        """
        Generates a dict from attributes to be converted to yaml
        """
        _model = dict()
        _model["kind"] = "Model"

        metadata = dict()
        metadata["name"] = self.name
        _model["metadata"] = metadata

        spec = dict()
        spec["storageUri"] = self.url

        requirements = ["sklearn"]
        spec["requirements"] = requirements

        spec["memory"] = self.memory
        spec["replicas"] = self.replicas

        _model["spec"] = spec

        return _model
