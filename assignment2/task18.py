# Authentication System
# ○ Task: Write a program to authenticate a user by validating their username and
# password.
# ○ Predefined Credentials:
# ■ Username: user1
# ■ Password: pass@123
# ○ Input: Prompt the user to input their username and password.
# ○ Output:
# ■ If the credentials match, display "Authentication successful."
# ■ If they do not match, display "Authentication failed."
valid_username = "user1"
valid_password = "pass@123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == valid_username and password == valid_password:
    print("Authentication successful.")
else:
    print("Authentication failed.")