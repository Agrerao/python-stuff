
while True:
    myInput = input("Enter a number: ")

    if myInput.isdigit():
        print("Your input: " + myInput)
        print("You completed it!")
        break
    else:
        print("Not a number?")

