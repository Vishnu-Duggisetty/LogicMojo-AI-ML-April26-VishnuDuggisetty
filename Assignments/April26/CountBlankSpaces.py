def countBlankSpaces(enteredValue):
    blankSpaces = 0
    for letter in enteredValue:
        if letter == " ":
            blankSpaces += 1
    return blankSpaces

enteredValue = str(input("Enter a value to count blank spaces:"))
if not enteredValue or len(enteredValue) == 0:
    print("No value entered. Hit me again.")
else:
    resultValue = countBlankSpaces(enteredValue)
    print(f"There are {resultValue} blank spaces in the entered value '{enteredValue}'.")