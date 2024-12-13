from math import log10
n = int(input("Enter a number: "))
n1 = n
# Brute Force Method
count = 0
while(n1>0):
    count = count + 1
    n1 = n1 // 10
print("Count using Brute Force Method: ", count)

# Optimal Method
count = 0
count = int(log10(n) + 1)
print("Count using Optimal Method: ",count)
