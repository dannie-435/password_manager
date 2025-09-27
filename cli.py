from functions import random_secure_string

while True:
    user_input_length = input("How many characters do you want in your password ? ( minimum 8 ) ")

    user_input_length = int(user_input_length)

    if user_input_length < 8:
        print("Your password must be 8 or more characters ")
        continue
    else:
        print(f"Your password will have a length of {user_input_length}")

    user_input_type = input("Include (letters, digits, specials) separated by a comma")

    use_letters = "letters" in user_input_type
    use_digits = "digits" in user_input_type
    use_specials = "specials" in user_input_type

    print(random_secure_string(user_input_length,use_letters,use_digits,use_specials))

