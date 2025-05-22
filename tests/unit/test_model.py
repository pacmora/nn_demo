import pytest
from pydantic import ValidationError

from src.model_generator.domain.model import Model


def test_model_name():
    # Replicas must be greater than zero, ValueError exception will be raised.
    with pytest.raises(ValidationError):
        model: Model = Model(
            name="ml",
            url="http://localhost:8080/models/my_model",
            memory="130Ki",
            replicas=1,
        )


def test_model_memory():
    # Memory format checker
    with pytest.raises(ValidationError):
        model: Model = Model(
            name="my_model",
            url="http://localhost:8080/models/my_model",
            memory="130Ku",
            replicas=0,
        )

        model: Model = Model(
            name="my_model",
            url="http://localhost:8080/models/my_model",
            memory="1K",
            replicas=1,
        )

        model: Model = Model(
            name="my_model",
            url="http://localhost:8080/models/my_model",
            memory="1Ku",
            replicas=1,
        )

        model: Model = Model(
            name="my_model",
            url="http://localhost:8080/models/my_model",
            memory="Ki",
            replicas=1,
        )


def test_model_replicas():
    # Replicas must be greater than zero, ValueError exception will be raised.
    with pytest.raises(ValidationError):
        model: Model = Model(
            name="my_model",
            url="http://localhost:8080/models/my_model",
            memory="130Ki",
            replicas=0,
        )


def test_model_generate_dict():
    expected_output = dict()
    expected_output["kind"] = "Model"

    metadata = dict()
    metadata["name"] = "my_model"
    expected_output["metadata"] = metadata

    spec = dict()
    spec["memory"] = "130Ki"
    spec["replicas"] = 1

    requirements = ["sklearn"]
    spec["requirements"] = requirements
    spec["storageUri"] = "http://localhost:8080/models/my_model"

    expected_output["spec"] = spec

    model: Model = Model(
        name="my_model",
        url="http://localhost:8080/models/my_model",
        memory="130Ki",
        replicas=1,
    )

    assert expected_output == model.model_to_dict()
