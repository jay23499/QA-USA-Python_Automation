# Retrieves Phone code. Do not change
# File should be completely unchanged


from typing import LiteralString

def retrieve_phone_code(driver) -> LiteralString | None:
    """

    :type driver: object
    """
    pass

def retrieve_phone_code(driver) -> str | None:
    """
    Retrieves the phone confirmation code from the application interface.

    Use this after the application has requested a confirmation code. This function waits for
    the code to appear in the UI and returns it as a string, or None if not found.

    :param driver: Selenium WebDriver instance used to access the web page.
    :return: The phone confirmation code as a string, or None if the code was not found.
    :raises WebDriverException: If Selenium encounters an error while locating elements.
    """


# Checks if Routes is up and running. Do not change
def is_url_reachable(url):
    """Check if the URL can be reached. Pass the URL for Urban Routes as a parameter.
    If it can be reached, it returns True, otherwise it returns False"""

    import ssl
    import urllib.request

    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
                 # print("Response Status Code:", response.status) #for debugging purposes
            if response.status == 200:
                return True
            else:
                return False
    except Exception as e:
        print(e)

    return False