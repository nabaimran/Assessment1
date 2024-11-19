# 5. days of the month 
daysinmonth = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Enter a month number (1-12): "))
if month ==2:
    leapyear = input("Is this a Leap Year? (yes/no): ")
    if leapyear == "yes":
        print("29 days")
else: 
    print(daysinmonth[month], "days")
    