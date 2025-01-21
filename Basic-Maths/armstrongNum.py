from math import log10
def isArmstrong(n):
    k = int(log10(n)+1)
    sum = 0
    num = n
    while(n > 0):
        lastDigit = n % 10
        sum = sum + lastDigit ** k
        n = n // 10
    return sum == num

if __name__ == "__main__":
    n = 371
    if isArmstrong(n):
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")