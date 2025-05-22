from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.auth.infrastructure.controller import router as auth_router
from src.model_generator.infrastructure.controller import (
    router as model_router,
)

app = FastAPI()
app.include_router(auth_router)
app.include_router(model_router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Demo NN",
        version="1.0.0",
        summary="Model generator API",
        description="This API allows to generate fancy models to be deployed in K8S",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
