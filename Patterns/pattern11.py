n = int(input("Enter a number: "))
for i in range(n):
    start = 1
    if i % 2 == 0: start = 1
    else: start = 0
    for j in range(i+1):
        print(start, end="")
        start = 1 - start
    print()
