import random

def get_secret(primary_key, primitive_root, private_key, public_key):
    calculation = public_key ** private_key
    secret = calculation % primary_key
    return secret


def get_keys():
    private_key = random.randint(10000 , 10000000)
    primitive_root = 5
    prime_number = 23
    public_key = (primitive_root ** private_key) % prime_number