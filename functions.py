import secrets
import string

def random_secure_string(length,use_letters=True,use_digits=False,use_specials=False):
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation

    return ''.join(secrets.choice(chars) for _ in range(length))

