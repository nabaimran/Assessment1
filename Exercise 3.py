# 3. Biography 
bio = {
    "name": "Naba Imran",
    "hometown": "Ajman",
    "age": 17
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")


# asking for user input 

name = input("What's your full name? ")
hometown = input("Where are you from? ")

# checking if age is an integer
while True:
        ageinput = input("Enter your age: ")
        if ageinput.isdigit():  
            age = int(ageinput)
            break
        else:
            print("That doesn't look like a number. Please try again.")

bio = {"name": name, 
"hometown": hometown, 
"age": age}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")

