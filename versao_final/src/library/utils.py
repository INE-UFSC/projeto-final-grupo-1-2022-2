import re
from typing import Any

CAMEL_REGEX = re.compile(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")

def snake_case(string: str) -> str:
    return CAMEL_REGEX.sub(r"_\1", string).lower()

def class_name(obj: Any):
    return snake_case(type(obj).__name__)