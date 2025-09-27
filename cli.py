from functions import random_secure_string

while True:
    user_input_length = input("How many characters do you want in your password ? ( minimum 8 ) ")

    user_input_length = int(user_input_length)

    if user_input_length < 8:
        print("Your password must be 8 or more characters ")
        continue

    # Password strength
    if user_input_length >= 16:
        print("Password Strength:Strong ")
    elif user_input_length >= 12:
        print("Password Strength:Medium ")
    elif user_input_length >= 8:
        print("Password Strength:Weak ")
    else:
        print(f"Your password will have a length of {user_input_length}")

    # Character type input
    user_input_type = input("Choose whether you want (letters, digits, specials) separated by a comma ( all three is recommended) ")
    user_input_type = [t.strip().lower() for t in user_input_type.split(",")]

    use_letters = "letters" in user_input_type
    use_digits = "digits" in user_input_type
    use_specials = "specials" in user_input_type

    # Guard clause
    if not(use_letters or use_digits or use_specials):
        print("Choose at least one and make sure you spell them correct separated by a comma" )
        continue

    # If only one type chosen
    if (use_letters + use_digits + use_specials) == 1:
        print("Next time consider using at least two types")

    # Combinations
    if use_letters and use_specials and use_digits:
        print("You chose to add letters, special characters and digits. With all three, your password is very strong")
    elif use_digits and use_specials:
        print("You chose to add digits and special characters.")
    elif use_specials and use_letters:
        print("You chose to add specials and letters.")
    elif use_digits and use_letters:
        print("You chose to add digits and letters.")

    #Generation of password
    print(f"Your password is {random_secure_string(user_input_length,use_letters,use_digits,use_specials)}")

