###
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
###

print("\n\n Diamond Pattern \n\n")
def printStarts(n):
    for i in range(n- 1):
        print(" " * (n - i) + "*" * (2 * i + 1), end=" ")
        print("")
    
    for i in range(n, 0, -1):
        print(" " +" " * (n - i) + "*" * (2 * i - 1), end=" ")
        print("")


printStarts(5)


print("\n\n Pyramid Pattern \n\n")
#     *
#    ***
#   *****
#  *******
# *********

def printPyramid(m):
    for i in range(m):
        print(" " * (m - i) + "*" * (2 * i + 1))


printPyramid(5)


# *****
# *   *
# *   *
# *   *
# *****
print("\n\n Hollow Square Pattern \n\n")

def printHallowSquare(n): 
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*") 

printHallowSquare(5)


# ***************
# **************
# *************
# ************
# ***********
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
print("\n\n Reverse staircase Pattern \n\n")

def printReverseStairCase(n):
    for i in range(n, 0, -1):
        print("*" * i)

printReverseStairCase(15)




def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        nums = nums1
        nums.extend(nums2)
        print(nums)
        lenNums = len(nums)
        middle = int(lenNums/2)

        if middle % 2 == 0:
            total = nums[middle] + nums[middle - 1]
            return float(total)
        else:
            return float(nums[middle])  
        
val = findMedianSortedArrays([1,2], [3])
print(val)