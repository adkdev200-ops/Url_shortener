import random
import string

characters = string.ascii_letters + string.digits
def rGenerator():
    text = ''.join(random.choice(characters) for _ in range(6))
    return text
