"""MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.
Examples:

Input: 26
Output: Z

Input: 51
Output: AY

Input: 52
Output: AZ

Input: 676
Output: YZ

Input: 702
Output: ZZ

Input: 704
Output: AAB"""





alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
def num_hash(num):
    if num < 26:
        return alpha[num-1]
    else:
        q, r = num//26, num % 26
        if r == 0:
            if q == 1:
                return alpha[r-1]
            else:
                return num_hash(q-1) + alpha[r-1]
        else:
            return num_hash(q) + alpha[r-1]
 
 
# Calling the function out here and printing the ALphabets
# This code is robust ,work for any positive integer only.
# You can try as much as you want
print(num_hash(26))
print(num_hash(51))
print(num_hash(52))
print(num_hash(80))
print(num_hash(676))
print(num_hash(702))
print(num_hash(705))
