import random 
def quicksort(arr, start , stop): 

    if(start < stop): 

        pivotindex = partitionrand(arr,start, stop) 
        quicksort(arr , start , pivotindex-1) 
        quicksort(arr, pivotindex + 1, stop) 
def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop) 
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop) 

def partition(arr,start,stop): 

    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot) 



array = []
print("Enter number of elements to sort")
size=int(input())
print("Enter input numbers:")
for i in range(size):
    s=int(input())
    array.append(s)
print("Unsorted Array")
print(array)

quicksort(array, 0, size - 1) 
print(array) 

''' OUTPUT
Enter number of elements to sort
8
Enter input numbers:
45
78
12
56
89
23
64
21
Unsorted Array
[45, 78, 12, 56, 89, 23, 64, 21]
[12, 21, 23, 45, 56, 64, 78, 89]
'''
