import random
import string

# Function to generate passwords
def generate_passwords(password_lengths):
    passwords = []

    for length in password_lengths:
        # Start with a random mix of letters
        password = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        
        # Add random numbers
        password = replace_with_number(password)
        
        # Add uppercase letters
        password = replace_with_uppercase_letter(password)

        passwords.append(password)

    return passwords

# Function to replace characters with numbers
def replace_with_number(password):
    for _ in range(random.randint(1, 2)):  # Replace 1-2 characters
        index = random.randint(0, len(password) - 1)
        password = password[:index] + str(random.randint(0, 9)) + password[index + 1:]
    return password

# Function to replace characters with uppercase letters
def replace_with_uppercase_letter(password):
    for _ in range(random.randint(1, 2)):  # Replace 1-2 characters
        index = random.randint(0, len(password) - 1)
        password = password[:index] + password[index].upper() + password[index + 1:]
    return password

# Main function
def main():
    print("Welcome to the Python Password Generator!")
    
    # Get the number of passwords to generate
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        if num_passwords < 1:
            print("You must generate at least one password.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Get the desired length for each password
    password_lengths = []
    print("Note: Minimum password length is 3.")
    for i in range(num_passwords):
        try:
            length = int(input(f"Enter the desired length for Password #{i + 1}: "))
            if length < 3:
                print("Password length too short. Setting length to 3.")
                length = 3
            password_lengths.append(length)
        except ValueError:
            print("Invalid input. Setting default length of 8.")
            password_lengths.append(8)

    # Generate and display the passwords
    passwords = generate_passwords(password_lengths)
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i}: {password}")


if __name__ == "__main__":
    main()
