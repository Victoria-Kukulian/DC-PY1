import string
from random import sample


def get_random_password(length=8) -> str:
    return ''.join(sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, length))


print(get_random_password())
