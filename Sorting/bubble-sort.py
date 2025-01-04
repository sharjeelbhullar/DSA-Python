def bubbleSort(self, arr):
    n = len(arr)
    for i in range(n-1, -1, -1): #loop from n-1 to 0
        for j in range(i): #loop from 0 to i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Optimized
def bubble_Sort(self, arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        didSwap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
        #Check if swap not done in first iteration then end the program as array is already sorted
        #Because this thing will make the TC more optimized Best [O(N)] if array is sorted 
        #Worst and average is O(N^2)
        if didSwap == 0:
            break