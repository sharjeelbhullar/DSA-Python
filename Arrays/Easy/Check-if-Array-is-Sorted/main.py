# Brute Force 
def checkArrayIsSorted(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                return False
            else:
                return True
            
# Optimal
def checkArray(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
        else:
            return True
        
if __name__ == "__main__":
    arr1 = [3, 2, 1, 4, 5]
    arr2 = [10, 20, 30, 40, 50]
    print(checkArrayIsSorted(arr1))
    print(checkArrayIsSorted(arr2))
    print(checkArray(arr1))
    print(checkArray(arr2))