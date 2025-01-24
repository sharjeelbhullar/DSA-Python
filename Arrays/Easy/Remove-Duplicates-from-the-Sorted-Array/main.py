# Brute Force Approach
from typing import List
def removeDup(arr: List[int]) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k

# Optimal Approach
def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i + 1

if __name__ == "__main__":
    arr1 = [1, 1, 2, 2, 2, 3, 3]
    arr2 = [1, 1, 2, 2, 2, 3, 3]
    k = removeDup(arr1)
    l = removeDuplicates(arr2)
    print("After using brute force approach: ")
    for i in range(k):
        print(arr1[i], end = " ")

    print("\nAfter using optimal approach: ")
    for i in range(l):
        print(arr2[i], end = " ")