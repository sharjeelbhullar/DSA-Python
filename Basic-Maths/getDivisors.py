#Brute Force Approach is O(N)
def printDivisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

#Optimal Approach is
def print_divisors(n):
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    
    print(" ".join(map(str, divisors)))

if __name__ == "__main__":
    n = int(input()) 
    print("Using Brute Force Method: ")
    printDivisors(n)
    print("\nUsing Optimal Method: ")
    print_divisors(n)
