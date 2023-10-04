
import string
import random

def gen_email(lenght, domain = "gmail.com", numeric = False):
    available_characters = string.ascii_lowercase
    email_main = ""
    
    if numeric:
        available_characters += string.digits

    for _ in range(lenght):
        character = random.choice(available_characters)
        email_main += character
        
    email_full = email_main + "@" + domain
    return email_full

print(gen_email(7))
print(gen_email(7,"wp.pl", True))
    
