import re

minimum_number = 9


def is_valid_password(password: str) -> bool:
    is_valid = True
    if len(password) < minimum_number:
        is_valid = False
    if not re.search(r'\d', password):
        is_valid = False
    if not re.search(r'[a-z]', password):
        is_valid = False
    if not re.search(r'[A-Z]', password):
        is_valid = False
    if not re.search(r'[!@#$%^&*()\-+]', password):
        is_valid = False
    if len(password) != len(set(password)):
        is_valid = False
    if ' ' in password:
        is_valid = False

    return is_valid
