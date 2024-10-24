def age_verification():
    print("Welcome to the Age Verification Program!")

    # Get user input for name
    user_name = input("Please enter your name: ")
    print("Hello, {user_name}! Let's verify your age.")

    # Get user input for age
    age_input = input("Please enter your age: ")

    # Check if the age is a valid number
    if age_input.isdigit():
        age = int(age_input)
        if age >= 18:
            print("Great, {user_name}! You are {age} years old, and you are eligible.")
        else:
            print("Sorry, {user_name}. You are {age} years old, so you are not eligible.")
    else:
        print("Invalid input! Please enter a valid number for your age.")

# Run the function
age_verification()




