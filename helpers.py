# helpers.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests


def create_driver():
    """Initialize the Chrome WebDriver and return driver and wait object"""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    return driver, wait


def is_url_reachable(url: str, timeout: int = 5) -> bool:
    """
    Check if a URL is reachable by sending a HEAD request.
    Returns True if status code is 200, False otherwise.
    """
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False
