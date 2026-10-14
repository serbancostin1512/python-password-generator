
import secrets
import string


def generate_password(length, use_digits=True, use_symbols=True):
    if length < 8:
        raise ValueError("Password length must be at least 8. ")

    characters = string.ascii_letters
    password_chars = []

    if use_digits :
        characters += string.digits
        password_chars.append(secrets.choice(string.digits))
    
    if use_symbols:
        characters += string.punctuation
        password_chars.append(secrets.choice(string.punctuation))

    while len(password_chars) < length :
        password_chars.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

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
