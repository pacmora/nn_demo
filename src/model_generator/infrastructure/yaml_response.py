from typing import Any

from fastapi import Response
from yaml import dump

"""Custom response class to convert a dict into yaml plain text response.
    Furthermore this class improve /docs information.

"""


class YAMLResponse(Response):
    media_type = "text/yaml"

    def render(self, content: Any) -> bytes | memoryview:
        return dump(content, encoding="utf-8")
