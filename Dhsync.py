import random
from utils.secret import get_secret, get_keys

def initialization():
    print("Dhsync initialization \n")
    get_keys()
    print("Do you want to Communicate with another user? (y/n)")
