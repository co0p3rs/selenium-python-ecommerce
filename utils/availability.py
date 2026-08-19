from urllib.error import URLError
from urllib.request import Request, urlopen


def is_available(url: str, timeout: float = 5.0) -> bool:
    try:
        with urlopen(Request(url, method="HEAD"), timeout=timeout) as response:
            return response.status < 500
    except (URLError, TimeoutError):
        return False

