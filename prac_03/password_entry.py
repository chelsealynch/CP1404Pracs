"""
Chelsea Lynch
"""

MINIMUM_LENGTH = 4


def version_1():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    print('*' * len(password))


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    password = input("Enter a password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Your password is too short.")
        password = input("Enter a password of at least {} characters: ".format(MINIMUM_LENGTH))
    return get_password(MINIMUM_LENGTH)


def print_asterisks(sequence):
    print('*' * len(sequence))

main()
