"""Given a matrix that is organized such that the numbers will always be sorted left to right, and the first number of each row will always be greater than the last element of the last row (mat[i][0] > mat[i - 1][-1]), search for a specific value in the matrix and return whether it exists.

Here's an example and some starter code.

def searchMatrix(mat, value):
  # Fill this in.
  
mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
"""

# Python program to search an element in row-wise
# and column-wise sorted matrix

# Searches the element x in mat[][]. If the
# element is found, then prints its position
# and returns true, otherwise prints "not found"
# and returns false
def search(mat, n, x):
	if(n == 0):
		return -1
	
	# Traverse through the matrix
	for i in range(n):
		for j in range(n):
			
			# If the element is found
			if(mat[i][j] == x):
				print("Element found at (", i, ",", j, ")")
				return 1
	
	print(" Element not found")
	return 0

# Driver code
mat = [[10, 20, 30, 40], [15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
search(mat, 4, 29)

# This code is contributed by rag2127
