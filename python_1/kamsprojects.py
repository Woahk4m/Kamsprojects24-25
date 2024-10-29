def age_verification():
    print("Welcome to the RACES WITH KAM!")

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

def main():
    accounts = {}
    
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def customize_car():
    print("Welcome to the Car Customization!")
    
    # Get the car tag from the user
    tag = input("Enter a tag for your car (e.g., 'FastCar123'): ")

    # Choose a car model
    print("Choose your car model:")
    models = ["Sedan", "SUV", "Sports Car", "Truck"]
    for i, model in enumerate(models, start=1):
        print(f"{i}. {model}")
    
    model_choice = int(input("Enter the number corresponding to your choice: "))
    
    if 1 <= model_choice <= len(models):
        chosen_model = models[model_choice - 1]
    else:
        print("Invalid choice, defaulting to 'Sedan'.")
        chosen_model = "Sedan"

    # Customize car color
    print("Choose a color for your car:")
    colors = ["Red", "Blue", "Green", "Black", "White"]
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")

    color_choice = int(input("Enter the number corresponding to your choice: "))
    
    if 1 <= color_choice <= len(colors):
        chosen_color = colors[color_choice - 1]
    else:
        print("Invalid choice, defaulting to 'Black'.")
        chosen_color = "Black"

    # Summary of customization
    print("\nCustomization Summary:")
    print(f"Car Tag: {tag}")
    print(f"Car Model: {chosen_model}")
    print(f"Car Color: {chosen_color}")

if __name__ == "__main__":
    customize_car()

import keyboard  # Make sure to install the keyboard library with `pip install keyboard`

def show_instructions():
    print("\nInstructions:")
    print("1. Use 'W' to accelerate.")
    print("2. Use 'S' to brake.")
    print("3. Use 'A' to turn left.")
    print("4. Use 'D' to turn right.")
    print("5. Use arrow keys for directional control.")
    print("6. Press 'Q' to quit the simulation.\n")

def main():
    print("Welcome to the Car Simulation Game!")
    
    while True:
        choice = input("Do you want to see the instructions? (yes/no): ").strip().lower()
        
        if choice == 'yes':
            show_instructions()
            break  # Exit the loop to proceed to the simulation
        elif choice == 'no':
            print("Skipping instructions...")
            break  # Exit the loop to proceed to the simulation
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    # Proceed to the car simulation (placeholder)
    print("Starting the car simulation...")

if __name__ == "__main__":
    main()


def car_simulation():
    print("Car Simulation Started!")
    print("Controls:")
    print("W - Accelerate")
    print("S - Brake")
    print("A - Turn Left")
    print("D - Turn Right")
    print("Arrow Keys - Direction Control")
    print("Press 'Q' to Quit\n")

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

if __name__ == "__main__":
    car_simulation()


