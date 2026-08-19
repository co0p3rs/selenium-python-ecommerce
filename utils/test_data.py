from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class Customer:
    first_name: str
    last_name: str
    postal_code: str


def unique_customer() -> Customer:
    suffix = uuid4().hex[:8]
    return Customer(first_name=f"Test{suffix}", last_name="User", postal_code="10001")

