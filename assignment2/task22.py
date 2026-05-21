# Menu-Driven Login System
# 1. Create the Menu:
# ○ Display a menu with three choices for the user:
# ■ Login with Phone
# ■ Login with Email
# ■ Exit the system
# 2. Predefined Credentials:
# ○ Phone number: "1234567890"
# ○ OTP: "1234"
# ○ Email: "user@example.com"
# ○ Password: "password123”
# 3. Login Functionality:
# ○ Option 1 (Login with Phone):
# ■ Prompt the user to enter their phone number and OTP.
# ■ Compare the input with a predefined phone number and OTP.
# ■ Display success if both match or an error message if they don’t.
# ○ Option 2 (Login with Email):
# ■ Prompt the user to enter their email and password.
# ■ Compare the input with predefined email and password.
# ■ Display success if both match or an error message if they don’t.
# ○ Option 3 (Exit):
# ■ Display an exit message and terminate the program.
# ○ Invalid Input:
# ■ Handle invalid user choices and ask the user to select a valid option.
# Output:
# 1. If the user enters a valid phone number and OTP, display: "Login successful
# with phone!"
# 2. If the user enters valid email and password, display: "Login successful
# with email!"
# 3. If the user selects the exit option, display: "Exiting the program. Have a
# nice day!"
# 4. If the user enters invalid credentials or an invalid choice, display appropriate error
# messages.
valid_phone = "1234567890"
valid_otp = "1234"
valid_email = "user@example.com"
valid_password = "password123"
while True:
    print("Menu:")
    print("1. Login with Phone")
    print("2. Login with Email")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        phone = input("Enter your phone number: ")
        otp = input("Enter the OTP: ")
        if phone == valid_phone and otp == valid_otp:
            print("Login successful with phone!")
        else:
            print("Invalid phone number or OTP. Please try again.")
    
    elif choice == "2":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == valid_email and password == valid_password:
            print("Login successful with email!")
        else:
            print("Invalid email or password. Please try again.")
    
    elif choice == "3":
        print("Exiting the program. Have a nice day!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1, 2, or 3).")