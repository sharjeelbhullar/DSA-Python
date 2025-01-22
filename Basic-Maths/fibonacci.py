n = int(input("Enter the number of terms: "))
if n == 0:
    print(f"The Fibonacci Series up to {n}th term:")
    print(0)
else:
    secondLast = 0  # (i-2)th term
    last = 1  # (i-1)th term
    print(f"The Fibonacci Series up to {n}th term:")
    print(secondLast, last, end=" ")
    for i in range(2, n + 1):
        cur = last + secondLast
        secondLast = last
        last = cur
        print(cur, end=" ")

