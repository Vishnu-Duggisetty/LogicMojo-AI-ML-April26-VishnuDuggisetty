def findVowels(enteredValue):
    vowels = "aeiouAEIOU"
    # foundVowels = [lett for lett in enteredValue if lett in vowels] ## This is a list comprehension technique to find vowels in the entered value
    ## The below code is a manual way to find vowels in the entered value without using list comprehension
    foundVowels = []
    for lett in enteredValue:
        if lett in vowels:
            foundVowels.append(lett)
    return foundVowels

enteredValue = str(input("Enter a value to find vowels:"))
if not enteredValue or len(enteredValue) == 0:
    print("No value entered. Hit me again.")
else:    
    resultValue = findVowels(enteredValue)
    if len(resultValue) > 0:
        print(f"The vowels in the entered value '{enteredValue}' are: {', '.join(resultValue)}")
    else:
        print(f"There are no vowels in the entered value '{enteredValue}'.")