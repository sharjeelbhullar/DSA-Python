# n = int(input("Enter a number: "))
# dup = n
# reverse = 0
# while(dup > 0):
#     lastDigit = dup % 10
#     reverse = reverse * 10 + lastDigit
#     dup = dup // 10
# if reverse == n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

x = int(input("Enter a number: "))
sign = -1 if x < 0 else 1
x = abs(x)
reverse = 0
while(x > 0):
    lastDigit = x % 10
    reverse = reverse * 10 + lastDigit
    x //= 10
print(sign * reverse)