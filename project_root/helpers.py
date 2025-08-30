from requests import head, RequestException

def is_url_reachable(url: str, timeout: int = 5) -> bool:
    """
    Returns True if the server responds (even with 404), False if server is unreachable.
    """
    try:
        response = head(url, timeout=timeout)
        return response.status_code < 500
    except RequestException:
        return False
