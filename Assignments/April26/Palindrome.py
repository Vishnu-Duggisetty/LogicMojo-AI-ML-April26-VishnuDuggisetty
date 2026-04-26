def checkPalindrome(enteredValue):
    if enteredValue == enteredValue[::-1]:
        return True
    else:
        return False


enteredValue = str(input("Enter a value to check for Palindrome:"))
resultValue = checkPalindrome(enteredValue)
if resultValue:
    print(f"{enteredValue} is a Palindrome")
else:
    print(f"{enteredValue} is NOT a Palindrome")


