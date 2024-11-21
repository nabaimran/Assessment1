# 6. Brute Force Attack 
 
correct_password = "12345"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Password correct!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Wrong password. {remaining_attempts} attempts remaining.")
        if remaining_attempts == 0:
            print("Max attempts reached.")
