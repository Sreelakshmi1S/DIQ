"""An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:

Input: 1592551013
Output: ['159.255.101.3', '159.255.10.13']  """






def is_valid(ip):
 
    # Splitting by "."
    ip = ip.split(".")
     
    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                          int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
            i[0] == '0'):
            return False
             
    return True
 
# Function converts string to IP address
def convert(s):
     
    sz = len(s)
    print(sz)
 
    # Check for string size
    if sz > 12:
        return []
    snew = s
    l = []
 
    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]
                 
                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)
                     
                snew = s
                 
    return l
 
# Driver code        

B = "25505011535"
 
A = "25525511135"
print(convert(B))
print(convert(A))
