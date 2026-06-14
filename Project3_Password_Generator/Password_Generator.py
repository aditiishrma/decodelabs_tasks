import secrets
import string
import os


# ===============================
# STARTUP BANNER
# ===============================

def banner():

    print("\n")
    print("=" * 50)
    print("   ENTERPRISE PASSWORD GENERATOR SYSTEM")
    print("      Secure • Fast • Professional")
    print("=" * 50)


# ===============================
# PASSWORD GENERATION
# ===============================

def generate_password(length):

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(

        secrets.choice(characters)

        for _ in range(length)

    )

    return password


# ===============================
# PASSWORD STRENGTH
# ===============================

def password_strength(length):

    if length >= 16:

        return (
            "★★★★★",
            "HIGH SECURITY"
        )

    elif length >= 10:

        return (
            "★★★★",
            "MEDIUM SECURITY"
        )

    else:

        return (
            "★★",
            "LOW SECURITY"
        )


# ===============================
# SAVE PASSWORD
# ===============================

def save_password(password):

    with open(
        "passwords.txt",
        "a"
    ) as file:

        file.write(

            password

            + "\n"

        )


# ===============================
# VIEW SAVED PASSWORDS
# ===============================

def view_passwords():

    if not os.path.exists(

            "passwords.txt"

    ):

        print("\nNo Saved Passwords.\n")

        return

    print("\n===== SAVED PASSWORDS =====")

    with open(

            "passwords.txt",

            "r"

    ) as file:

        data = file.readlines()

        if not data:

            print("No Passwords Found")

        else:

            for number, value in enumerate(

                    data,

                    start=1

            ):

                print(

                    f"{number}. "

                    f"{value.strip()}"

                )


# ===============================
# MAIN MENU
# ===============================

def menu():

    banner()

    while True:

        print("\n")

        print("1. Generate Password")

        print("2. View Saved Passwords")

        print("3. Exit")

        choice = input(

            "\nEnter Choice: "

        )

        if choice == "1":

            try:

                length = int(

                    input(

                        "\nEnter Password Length: "

                    )

                )

                if length < 6:

                    print(

                        "Minimum Length = 6"

                    )

                    continue

                password = (

                    generate_password(

                        length

                    )

                )

                strength, security = (

                    password_strength(

                        length

                    )

                )

                print("\n")

                print("=" * 40)

                print(

                    "Generated Password:\n"

                )

                print(password)

                print(

                    "\nPassword Strength:",

                    strength

                )

                print(

                    "Estimated Security:",

                    security

                )

                print("=" * 40)

                save = input(

                    "\nSave Password? (Y/N): "

                ).upper()

                if save == "Y":

                    save_password(

                        password

                    )

                    print(

                        "Password Saved!"

                    )

            except ValueError:

                print(

                    "Invalid Input!"

                )

        elif choice == "2":

            view_passwords()

        elif choice == "3":

            print(

                "\nThank You!"

            )

            break

        else:

            print(

                "Invalid Choice!"

            )


menu()