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



## using 2 pointers

def checkPalindromeUsing2Pointers(enteredValue): 
    left = 0
    right = len(enteredValue) - 1

    while left < right:
        if enteredValue[left] != enteredValue[right]:
            return False
        left += 1
        right -= 1
    return True

myValue = str(input("Enter a value to check for Palindrome:"))
myResultValue = checkPalindromeUsing2Pointers(myValue)

if myResultValue:
    print(f"{myValue} is a Palindrome using 2 pointers")
else:    
    print(f"{myValue} is NOT a Palindrome using 2 pointers")

