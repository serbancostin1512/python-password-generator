
import secrets
import string


def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters

    if use_digits :
        characters += string.digits
    
    if use_symbols:
        characters += string.punctuation
    
    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("=== PASSWORD GENERATOR ===")

    try:
        length = int(input("Password length is minimum 8 : "))

        if length < 8 :
            print("Error: password must have at least 8 characters. ")
            return

        digits_answer = input("Include digits ? (y/n)").lower()
        symbols_answer = input("Include symbols ? (y/n)").lower()

        use_digits = digits_answer == "y"
        use_symbols = symbols_answer == "y"
        
        password = generate_password(
            length,
            use_digits,
            use_symbols
        )

        print("\nGenerated password :", password)

    except ValueError:
        print("Error : enter a valid integer. ")
if __name__ == "__main__":
    main()
