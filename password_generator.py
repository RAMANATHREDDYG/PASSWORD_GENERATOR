import random
import string

# Function to generate a single password
def generate_password(password_length):
    # Initialize the password with one character from each character set
    password = random.choices(string.ascii_uppercase)[0]  # Add a random uppercase letter
    password += random.choices(string.ascii_lowercase)[0]  # Add a random lowercase letter
    password += random.choices(string.digits)[0]  # Add a random digit
    password += random.choices(string.punctuation)[0]  # Add a random punctuation/special character

    # If password length is greater than or equal to 5, add remaining characters randomly
    if password_length >= 5:
        remaining_length = password_length - 4  # Calculate the remaining length after adding mandatory characters
        # Generate remaining characters using a combination of letters, digits, and punctuation
        password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))
        # Shuffle the password characters to ensure randomness
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

    return password

# Function to generate multiple passwords
def generate_passwords(num_of_passwords, password_length):
    # Generate passwords using the generate_password function and list comprehension
    passwords = [generate_password(password_length) for _ in range(num_of_passwords)]
    return passwords

# Function to validate user input
def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

try:
    # Prompt user for the number of passwords and password length
    num_of_passwords = validate_input("Enter the number of passwords to generate: ")
    password_length = validate_input("Enter the length of each password: ")

    # Check if password length is valid (greater than 3)
    if password_length <= 3:
        raise ValueError("Password length must be greater than 3")

    # Generate passwords
    passwords = generate_passwords(num_of_passwords, password_length)

    # Print generated passwords
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

# Handle exceptions
except ValueError as e:
    print(e)
