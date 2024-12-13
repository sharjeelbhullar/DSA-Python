n = int(input("Enter a number: "))
dup = n
reverse = 0
while(dup > 0):
    lastDigit = dup % 10
    reverse = reverse * 10 + lastDigit
    dup = dup // 10
if reverse == n:
    print("Palindrome")
else:
    print("Not Palindrome")
