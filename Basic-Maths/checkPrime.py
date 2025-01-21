#Brute Force Approach is O(N)
def check_prime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

#Optimal Approach is O(sqrt(N))
def checkPrime(n):
    cnt = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1

            if n // i != i:
                cnt += 1

    if cnt == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 1483
    is_prime = checkPrime(n)
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
