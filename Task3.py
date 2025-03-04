def assess_password_strength(password):
    # Check if the password has at least 8 characters
    pswd_length = len(password) >= 8

    # Check if the password has at least one uppercase letter
    upper_case = False
    for char in password:
        if char.isupper():
            upper_case = True
            break

    # Check if the password has at least one lowercase letter
    lower_case = False
    for char in password:
        if char.islower():
            lower_case = True
            break

    # Check if the password has at least one number
    number = False
    for char in password:
        if char.isdigit():
            number = True
            break

    # Check if the password has at least one special character
    specialChar = False
    for char in password:
        if char in "!@#$%^&*()_+":
            specialChar = True
            break

    
    if not pswd_length:
        print("Password should be at least 8 characters long.")
    if not upper_case:
        print("Password should have at least one uppercase letter.")
    if not lower_case:
        print("Password should have at least one lowercase letter.")
    if not number:
        print("Password should have at least one number.")
    if not specialChar:
        print("Password should have at least one special character.")

    
    if pswd_length and upper_case and lower_case and number and specialChar:
        print("Your password is Strong!")
    elif pswd_length:
        print("Your password is Medium.")
    else:
        print("Your password is Weak.")


password = input("Enter your password: ")
assess_password_strength(password)
