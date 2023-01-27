import re

def isValidEmail(email_string: str):
    """"
        * Check if {email_string} is a valid email address
    """
    if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email_string):
        return True
    return False
