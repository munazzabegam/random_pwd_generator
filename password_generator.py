import string
import random

def generate_password(length=12, use_special_chars=True):
    pwd_characters = string.ascii_letters + string.digits
    if use_special_chars:
        pwd_characters += string.punctuation
    
    required_characters = [string.ascii_uppercase, string.ascii_lowercase, string.digits]
    
    password = ''.join(random.choices(pwd_characters, k=length))
    
    for char_type in required_characters:
        if not any(char in password for char in char_type):
            replace_index = random.randint(0, length - 1)
            password = (password[:replace_index] + 
                        random.choice(char_type) + 
                        password[replace_index + 1:])
    
    return password
