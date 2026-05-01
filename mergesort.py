import time
import random
def merge(arr, l, m, h):  
    L = []  
    R = []  
    n1 = m - l + 1  
    n2 = h - m  
     
    for i in range(0, n1):  
        L.append(arr[l + i])  
    for j in range(0, n2):  
        R.append(arr[m + 1 + j])  

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:  
        if L[i] <= R[j]:  
            arr[k] = L[i]  
            i += 1  
        else:  
            arr[k] = R[j]  
            j += 1  
        k += 1  

    # Copy remaining elements of L[]
    while i < n1:  
        arr[k] = L[i]  
        i += 1  
        k += 1  

    # Copy remaining elements of R[]
    while j < n2:  
        arr[k] = R[j]  
        j += 1  
        k += 1  

def mergesort(arr, l, h):  
    if l < h:  
        mid = l + (h - l) // 2  
        mergesort(arr, l, mid)  
        mergesort(arr, mid + 1, h)  
        merge(arr, l, mid, h)  
  

arr=[]
for i in range(1,100001): 
 elements=random.randint(1,100001)
 arr.append(elements)  
 
starting_time= time.time()
mergesort(arr, 0, len(arr) - 1) 
ending_time= time.time()
Time=ending_time-starting_time
print("time for MergeSort:",Time,"sec")
