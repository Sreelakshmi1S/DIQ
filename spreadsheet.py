"""Hi, here's your problem today. This problem was recently asked by Apple:

In many spreadsheet applications, the columns are marked with letters. From the 1st to the 26th column the letters are A to Z. Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc.

Given a number n, find the n-th column name."""




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
           
print(num_hash(26))
print(num_hash(27))
print(num_hash(28))
