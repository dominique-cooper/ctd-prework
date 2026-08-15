# This script greets the user and gives advice based on whether they track their spending.

name = input("What's your first name? ")
age = int(input("How old are you? "))

if age >= 18:
    print("Hi " + name + ", you are old enough to manage your finances.")
else:
    print("Hi " + name + ", start building good money habits now!")