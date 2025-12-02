import time
import random
def quicksort(arr):
  if(len(arr))<=1:
    return arr
  else:
   less=[]
   greater=[]
   pivot=arr[0]
   for x in arr[1:]:
     if x<=pivot:
       less.append(x) 
     else:
       greater.append(x)
  return quicksort(less) + [pivot] + quicksort(greater)
arr=[34,67,83,12,90,56,21]
#for i in range(1,1000001): 
 #elements=random.randint(1,1000000001)
 #arr.append(elements)

starting_time= time.time()
sorted_array=quicksort(arr)
ending_time= time.time()
Time=ending_time-starting_time
print("the sorted array is",sorted_array)

print("time for QuickSort:",Time,"sec")
