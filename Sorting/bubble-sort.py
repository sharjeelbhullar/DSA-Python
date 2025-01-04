def bubbleSort(self, arr):
    n = len(arr)
    for i in range(n-1, -1, -1): #loop from n-1 to 0
        for j in range(i): #loop from 0 to i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
