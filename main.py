import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus=minus.upper()

numbers = "0123456789"
symbols = "Δ€()@$%~<#>{}[]&;_-!?^*=+,."

base = minus+mayus+numbers+symbols

characters = 16

for _ in range(10):
    sample = random.sample(base, characters)
    password = "".join(sample)
    encrypted_password = generate_password_hash(password)
    print("{} → {}".format(password, encrypted_password))