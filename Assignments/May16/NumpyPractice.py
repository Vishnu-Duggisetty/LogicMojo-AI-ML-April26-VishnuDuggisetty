import numpy as np

print("Numpy Practice")

# check version
print(np.__version__)

print("********************** \n\n Question 1")
# Question : Create a 1D array of numbers from 0 to 9
# Output : #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = np.arange(10)
print(arr)


print("********************** \n\n Question 2")
# Question : Create a 3×3 numpy array of all True’s
# Output : #> array([[ True,  True,  True],

boolArr = np.ones((3, 3), dtype=bool)
print(boolArr)
boolArr = np.full((3, 3), True, dtype=bool)
print(boolArr)

print("********************** \n\n Question 3")
# Question : Extract all odd numbers from array
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([1, 3, 5, 7, 9])

inputArr1 = np.arange(10)
outputArr1 = inputArr1[inputArr1 % 2 == 1]
print(outputArr1)

print("********************** \n\n Question 4")
# Question: Replace all odd numbers in arr with -1
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

inputArray2 = np.arange(10)
outputArr2 = inputArray2.copy()
outputArr2[outputArr2 % 2 == 1] = -1
print(outputArr2)

print("********************** \n\n Question 5")
# Question: Convert a 1D array to a 2D array with 2 rows
# input: np.arange(10)
# output array([[0, 1, 2, 3, 4],
#               [5, 6, 7, 8, 9]])

inputArray3 = np.arange(10)
outputArr3 = inputArray3.reshape(2, -1)
print(outputArr3)


print("********************** \n \n Question 6")
# Question: Stack arrays a and b vertically
# input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)

# output: array([[0, 1, 2, 3, 4],
#                [5, 6, 7, 8, 9],
#                [1, 1, 1, 1, 1],
#                [1, 1, 1, 1, 1]])

inputArray4a = np.arange(10).reshape(2, -1)
inputArray4b = np.repeat(1, 10).reshape(2, -1)
outputArray4 = np.vstack([inputArray4a, inputArray4b])
print(outputArray4)

print("********************** \n \n Question 7")
# Question: Stack the arrays a and b horizontally.

# Input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)
# Output: array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#                [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])

inputArray5a = np.arange(10).reshape(2, -1)
inputArray5b = np.repeat(1, 10).reshape(2, -1)
outputArray5 = np.hstack([inputArray5a, inputArray5b])
print(outputArray5)


print("********************** \n \n Question 8")

# Question: Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

inputArray6 = np.array([1, 2, 3])
outputArray6 = np.concatenate([np.repeat(inputArray6, 3), np.tile(inputArray6, 3)])
print(outputArray6)

print("********************** \n \n Question 9")
# Question: Get the common items between a and b
# Input: a = np.array([1, 2, 3, 4, 5])
#        b = np.array([5, 6, 7, 8, 9])
# Output: array([5])
inputArray7a = np.array([1, 2, 3, 4, 5])
inputArray7b = np.array([5, 6, 7, 8, 9])
outputArray7 = np.intersect1d(inputArray7a, inputArray7b)
print(outputArray7)

# Question: From array a remove all items present in array b

# Input: a = np.array([1,2,3,4,5])
#        b = np.array([5,6,7,8,9])

# Output: array([1,2,3,4])
inputArray8a = np.array([1,2,3,4,5])
inputArray8b = np.array([5,6,7,8,9])
outputArray8 = np.setdiff1d(inputArray8a, inputArray8b)
print(outputArray8)

print("********************** \n \n Question 10")
# Question: Get the positions where elements of a and b match
# Input: a = np.array([1,2,3,4,5])
#        b = np.array([5,4,3,2,1])
# Output: array([2])
inputArray9a = np.array([1,2,3,4,5])
inputArray9b = np.array([5,4,3,2,1])
outputArray9 = np.where(inputArray9a == inputArray9b)[0]
print(outputArray9)

print("********************** \n \n Question 11")
# Question: Get all items between 5 and 10 from a.

# Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
# Output: (array([6, 9]),)
inputArray10 = np.array([2, 6, 1, 9, 10, 3, 27])
outputArr10 = inputArray10[(inputArray10 > 5) & (inputArray10 < 10)]
print(outputArr10)

print("********************** \n \n Question 12")
# Question: Convert the function maxx that works on two scalars, to work on two arrays.
# Input:

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

# maxx(1, 5)
#> 5

# Output:
# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])
# pair_max(a, b)
# array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])

inputArray11a = np.array([5, 7, 9, 8, 6, 4, 5])
inputArray11b = np.array([6, 3, 4, 8, 9, 7, 1])

def pair_max(x, y):
    """Get the maximum of two arrays element-wise"""
    return np.array([maxx(x, y) for x, y in zip(x, y)]).tolist()
outputArray11 = pair_max(inputArray11a, inputArray11b)
print(outputArray11)

print("********************** \n \n Question 13")
# Question: Swap columns 1 and 2 in the array arr.

# Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Output: array([[1, 3, 2],
#                [4, 6, 5],
#                [7, 9, 8]])
inputArray12 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
outputArray12 = inputArray12[:, [1,0,2]]
print(outputArray12)

print("********************** \n \n Question 14")
# Question: Swap rows 1 and 2 in the array arr.
# Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Output: array([[4, 5, 6],
#                [1, 2, 3],
#                [7, 8, 9]])
inputArray13 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
outputArray13 = inputArray13[[1,0,2], :]
print(outputArray13)

print("********************** \n \n Question 15")
# Question: Reverse the rows of a 2D array arr.
# Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Output: array([[7, 8, 9],
#                [4, 5, 6],
#                [1, 2, 3]])
inputArray14 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
outputArray14 = inputArray14[::-1, :]
print(outputArray14)

print("********************** \n \n Question 16")
# Question: Reverse the columns of a 2D array arr.
# Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Output: array([[3, 2, 1],
#                [6, 5, 4],
#                [9, 8, 7]])
inputArray15 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
outputArray15 = inputArray15[:, ::-1]
print(outputArray15)

print("********************** \n \n Question 17")
# Question: Create an array of shape (5, 3) with random values and sort each column in ascending order.
# Input: np.random.rand(5, 3)
# Output: array([[0.123, 0.456, 0.789],
#                [0.234, 0.567, 0.890],
#                [0.345, 0.678, 0.901],
#                [0.456, 0.789, 0.012],
#                [0.567, 0.890, 0.123]])
inputArray16 = np.random.rand(5, 3)
outputArray16 = np.sort(inputArray16, axis=0)
print(outputArray16)

print("********************** \n \n Question 18")
# Question: Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
# def uniform(
#     low: float = 0,
#     high: float = 1,
#     size: None = None
# ) -> float: ...
inputArray17 = np.random.uniform(5, 10, size=(5, 3))
print(inputArray17)
print(inputArray17[::2, ::2])




## STAtiSTICS: Mean, Median, Standard Deviation, Variance

sss = np.array([[1, 2, 3, 4], [3, 4, 2, 1]])
print(sss)
cc = np.mean(sss, axis=0)
print(cc)


#Median
vv = np.array([[3, 2, 3, 4, 5]])
dd = np.median(vv)
print(dd)

vv = np.array([[3, 2, 3, 4], [1, 2, 3, 4], [5, 4, 3, 2]])
dd = np.median(vv, axis=0)
print(dd)



#Variance
vv = np.array([[3, 2, 3, 4], [1, 2, 3, 4], [5, 4, 3, 2]])
dd = np.var(vv, axis=0)
print(dd)

## Variance is the average of the squared differences from the mean. 
# It measures how spread out the numbers in a dataset are. 
# A higher variance indicates that the data points are more spread out from the mean,
#  while a lower variance indicates that they are closer to the mean.  
# 
# ## Standard Deviation
vv = np.array([[3, 2, 3, 4], [1, 2, 3, 4], [5, 4, 3, 2]])
dd = np.std(vv, axis=0)
print(dd)  

# Standard deviation is the square root of the variance. 
# It provides a measure of the average distance of each data point from the mean. 
# A higher standard deviation indicates that the data points are more spread out from the mean,
# while a lower standard deviation indicates that they are closer to the mean.