#Brute Force Approach
def find_gcd_BruteForce(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2) + 1):
        
        if n1 % i == 0 and n2 % i == 0:
           
            gcd = i

    return gcd

#Better Approach
def find_gcd_BetterApproach(n1, n2): 
    for i in range(min(n1, n2), 0, -1):
        
        if n1 % i == 0 and n2 % i == 0:
            
            return i
    
    return 1

#Euclidean Algorithm
#Optimal Approach
def find_gcd_OptimalApproach(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a

def main():
    n1 = 20
    n2 = 15

    gcd = find_gcd_BruteForce(n1, n2)
    print("GCD of", n1, "and", n2, "is:", gcd)

    gcd = find_gcd_BetterApproach(n1, n2)
    print("GCD of", n1, "and", n2, "is:", gcd)

    gcd = find_gcd_OptimalApproach(n1, n2)
    print("GCD of", n1, "and", n2, "is:", gcd)


if __name__ == "__main__":
    main()
    
    