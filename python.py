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

def main():
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Do you want to include special characters? (y/n): ").lower() == 'y'
    
    if length < 6:
        print("Password length should be at least 6 characters.")
        return
    
    password = generate_password(length, use_special_chars)
    print("Your password is:", password)

if __name__ == "__main__":
    main()
