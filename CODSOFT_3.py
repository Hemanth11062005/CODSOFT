import random
import string


def generate_pass(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the passowrd to generate:"))
        if length <=0:
            print("Please enter a positive integer greater than zero")
            return
    except ValueError:
        print("Please enter a valid integer for the length of the password")
        return
    
    password = generate_pass(length)
    print("Generated Password:",password)
    
if __name__ == "__main__":
    main()
    