"""Return the longest run of 1s for a given integer n's binary representation.

Example:

Input: 242
Output: 4 """




def maxConsecutiveOnes(x):
 
    # Initialize result
    count = 0
  
    # Count the number of iterations to
    # reach x = 0.
    while (x!=0):
     
        # This operation reduces length
        # of every sequence of 1s by one.
        x = (x & (x << 1))
  
        count=count+1
     
    return count
 
# Driver code
 
print(maxConsecutiveOnes(242))
print(maxConsecutiveOnes(4))
