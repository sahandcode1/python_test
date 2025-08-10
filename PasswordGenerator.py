import string
import random

def Password_Generator(len):
    chars = string.ascii_letters + string.digits + string.punctuation 
    return ''.join(random.choices(chars,k = len))  #This function selects len random characters from chars
print(Password_Generator(16))
