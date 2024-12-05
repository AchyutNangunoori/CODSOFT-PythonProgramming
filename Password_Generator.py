import random
import string

def generate_password():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 8:
            print("Password length should be at least 8 characters for strong security.")
            return
        
        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
        include_symbols = input("Include special characters? (y/n): ").strip().lower() == "y"
        
        if not (include_uppercase or include_lowercase or include_numbers or include_symbols):
            print("You must include at least one type of character!")
            return
        
        char_pool = ""
        if include_uppercase:
            char_pool += string.ascii_uppercase
        if include_lowercase:
            char_pool += string.ascii_lowercase
        if include_numbers:
            char_pool += string.digits
        if include_symbols:
            special_symbols = "!@#$%^&*()_-+=?"
            char_pool += special_symbols
        
        password = ''.join(random.choice(char_pool) for _ in range(length))
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    generate_password()
