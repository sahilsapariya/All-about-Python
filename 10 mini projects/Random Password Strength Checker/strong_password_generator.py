import random

def generate_password(password_length: int, lower_len: int, upper_len: int, numbers_len: int, symbol_len: int) -> str:
    """
    Returns: (str) strong password
    """

    def get_random_string(string: str, length: int) -> str:
        return "".join(random.sample(string, length))

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "@#$&_-()=%*:/!?+."

    try:
        strong_string = "".join([get_random_string(lower, lower_len),
                                get_random_string(upper, upper_len),
                                get_random_string(numbers, numbers_len),
                                get_random_string(symbols, symbol_len)])

        password = "".join(random.sample(strong_string, password_length))
        return password
    except ValueError:
        print("sum of the numbers is not equal to entered length of password")
        exit(0)


if __name__ == "__main__":
    password_len = int(input("How many of characters do you want to generate password (Recomanded 8 to 12) : "))
    lower_len  = int(input("Enter number of lower characters: "))
    upper_len  = int(input("Enter number of upper characters: "))
    numbers_len = int(input("Enter number of numbers : "))
    symbol_len  = int(input("Enter number of symbols : "))

    password = generate_password(password_len, lower_len, upper_len, numbers_len, symbol_len)

    print("Your password is : ", password)