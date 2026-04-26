def reverseString(enteredValue):
    ## return enteredValue[::-1]  ## This is a slicing technique to reverse the string
    ## The below code is a manual way to reverse the string without using slicing
    resultValue = ""
    for letter in enteredValue:
        resultValue = letter + resultValue
    return resultValue

enteredValue = str(input("Enter a string to reverse:"))
if not enteredValue or len(enteredValue) == 0:
    print("No value entered. Hit me again.")
else:
    resultValue = reverseString(enteredValue)
    print(f"The reversed string for '{enteredValue}' is: '{resultValue}'")