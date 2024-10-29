import keyboard  # Make sure to install the keyboard library with `pip install keyboard`

def age_verification():
    print("Welcome to the RACES WITH KAM!")

    # Get user input for name
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Let's verify your age.")

    # Get user input for age
    age_input = input("Please enter your age: ")

    # Check if the age is a valid number
    if age_input.isdigit():
        age = int(age_input)
        if age >= 18:
            print(f"Great, {user_name}! You are {age} years old, and you are eligible.")
            return True
        else:
            print(f"Sorry, {user_name}. You are {age} years old, so you are not eligible.")
            return False
    else:
        print("Invalid input! Please enter a valid number for your age.")
        return False

def create_account(accounts):
    username = input("Enter a new username: ")
    if username in accounts:
        print("Username already exists. Please choose a different one.")
    else:
        password = input("Create a password: ")
        accounts[username] = password
        print("Account created successfully!")

def login(accounts):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in accounts and accounts[username] == password:
        print("Login successful! Welcome back!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def choose_car_model():
    print("Choose your car type:")
    car_types = ["Sedan", "SUV", "Sports Car", "Truck"]
    
    for i, car_type in enumerate(car_types, start=1):
        print(f"{i}. {car_type}")

    while True:
        try:
            type_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= type_choice <= len(car_types):
                chosen_type = car_types[type_choice - 1]
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(car_types)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Choose specific car models based on type
    if chosen_type == "Sedan":
        models = ["Toyota Camry", "Honda Accord", "Ford Fusion"]
    elif chosen_type == "SUV":
        models = ["Toyota RAV4", "Honda CR-V", "Ford Explorer"]
    elif chosen_type == "Sports Car":
        models = ["Ferrari 488", "Porsche 911", "Chevrolet Corvette"]
    elif chosen_type == "Truck":
        models = ["Ford F-150", "Chevrolet Silverado", "Ram 1500"]

    print(f"\nChoose your car model for {chosen_type}:")
    for i, model in enumerate(models, start=1):
        print(f"{i}. {model}")

    while True:
        try:
            model_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= model_choice <= len(models):
                chosen_model = models[model_choice - 1]
                return chosen_type, chosen_model
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(models)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def customize_car():
    print("Welcome to the Car Customization!")
    
    # Get the car tag from the user
    tag = input("Enter a tag for your car (e.g., 'FastCar123'): ")
    
    # Choose car model
    chosen_type, chosen_model = choose_car_model()

    # Choose a color for your car
    print("Choose a color for your car:")
    colors = ["Red", "Blue", "Green", "Black", "White", "Pink", "Grey"]
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")

    while True:
        try:
            color_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= color_choice <= len(colors):
                chosen_color = colors[color_choice - 1]
                break
            else:
                print("Invalid choice, defaulting to 'Black'.")
                chosen_color = "Black"
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Summary of customization
    print("\nCustomization Summary:")
    print(f"Car Tag: {tag}")
    print(f"Car Model: {chosen_model}")
    print(f"Car Color: {chosen_color}")

def show_instructions():
    print("\nInstructions:")
    print("1. Use 'W' to accelerate.")
    print("2. Use 'S' to brake.")
    print("3. Use 'A' to turn left.")
    print("4. Use 'D' to turn right.")
    print("5. Use arrow keys for directional control.")
    print("6. Press 'Q' to quit the simulation.\n")

def car_simulation():
    print("Car Simulation Started!")
    show_instructions()

    while True:
        if keyboard.is_pressed('w'):
            print("Accelerating...")
        elif keyboard.is_pressed('s'):
            print("Braking...")
        elif keyboard.is_pressed('a'):
            print("Turning Left...")
        elif keyboard.is_pressed('d'):
            print("Turning Right...")
        elif keyboard.is_pressed('up'):
            print("Moving Up...")
        elif keyboard.is_pressed('down'):
            print("Moving Down...")
        elif keyboard.is_pressed('left'):
            print("Moving Left...")
        elif keyboard.is_pressed('right'):
            print("Moving Right...")
        elif keyboard.is_pressed('q'):
            print("Exiting the simulation. Thanks for playing!")
            break

def main():
    accounts = {}
    
    if not age_verification():
        return  # Exit if the age verification fails
    
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            if login(accounts):
                break  # Exit the loop if login is successful
        elif choice == '3':
            print("Exiting the program.")
            return
        else:
            print("Invalid choice. Please try again.")

    customize_car()
    car_simulation()

if __name__ == "__main__":
    main()
