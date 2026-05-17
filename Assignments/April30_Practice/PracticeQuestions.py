# You are planning to go to your friend's wedding and you have long events all month, lasting at least a few days. You have the start and end dates of events and your task is to find out events overlapping with the wedding date.

# The code for taking input has already been written for you, please don't modify that, but do read and try to understand the way input has been taken. You will be asked to take input on your own for most of the problems here onwards. Taking data in a suitable format is an important skill for a Data Scientist.

# ----------------------------------------------------------------------
# Input:
# The input will contain a list of lists where each sub-list has only two elements representing the start and end date of an event, the start date will be less than or equal to the end date. The next line of input will have a wedding date.

# Output:
# The output should have the number of events overlapping with the wedding date.

# ----------------------------------------------------------------------
# Sample input:
# [ [29,31], [23,26], [24,25] ]
# 24

# Sample output:
# 2

def countOverlappingEvents(events: list[list[int]], weddingDate: int) -> int:
    count = 0
    for event in events:
        if weddingDate in range(event[0], event[1] + 1):
            count += 1
    return count

# events = eval(input("Enter the list of events (as a list of lists with start and end dates):"))
# weddingDate = int(input("Enter the wedding date:"))
# print(countOverlappingEvents(events, weddingDate))




# Write a Python program to divide a given list into chunks of size k.

# The number of elements in the list need not to be divisible by k.
# For example, if you want to divide the list [1,2,3,4,5,6,7] into chunk size k=4, then the first chunk will be [1,2,3,4] and the second one will have [5,6,7]. i.e. the last chunk need not have k elements.
# The input will have two lines, the first line would have the list and the second line would have the value of k.(the code for taking input has already been written, you should not change that)
# The final output should have the list chunks in different lines.

# Sample Input:
# [1,2,3,4,5,6,7,8,9]
# 3
# Sample Output:

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

n = [1,2,3,4,5,6,7,8,9]
k = 3
def divideList():
    for i in range(0, len(n), k):
        print(n[i:i+k])

divideList()


# Given a list of numbers, find the second largest number in the list.

# Note: There might be repeated numbers in the list.
#  If there is only one number present in the list, return 'not present'.

# Examples:
# Input 1:
# [7, 2, 0, 9, -1, 8]
# Output 1:
# 8

def findSecondLargest(nums: list[int]) -> int:
    vals = set(nums)
    if len(vals) < 2:
        return "not present"
    maxval = 0
    minval = 0
    for num in list(vals):
        if num >= maxval:
            minval = maxval
            maxval = num
    return minval


nums = [7, 2, 0, 9, -1, 8]
print(findSecondLargest(nums))


# Your team is going for camping and you are taking a vote to decide what food to pack for dinner.
# Everyone gets a vote and the food item that gets at least one more than half of the votes wins.
#  None of the items wins if nothing gets at least one more than half votes. Assume that every person gets only one vote.
# The input will contain a list of food items where each occurrence of an item represents one vote. You should print the winning food item as output. If there is no clear winner, print "NOTA".

# Sample Input:
# ["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
# Sample Output:
# pasta

def findWinningFood(votes: list[str]) -> str:
    arrList = votes
    setArray = list(set(arrList))
    maxCount = 0
    winningItem = ""

    for item in setArray:
        count = arrList.count(item)
        if count > maxCount:
            maxCount = count
            winningItem = item

    return winningItem if maxCount > len(votes) / 2 else "NOT available"


votes = ["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
print(findWinningFood(votes))