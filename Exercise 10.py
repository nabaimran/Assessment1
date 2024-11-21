# 10. Is it even?

def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    # getting user input 
    number = int(input("Enter a number: "))
    result = even_odd(number)  # Corrected function name
    print(f"The number is {result}.")

# Call the main function
main()



