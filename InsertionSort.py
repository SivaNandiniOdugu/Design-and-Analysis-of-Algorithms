def Insertion_sort(arr):
    n = len(arr) ;BI_count[0]+=1

    for i in range(1, n):
        temp = arr[i]; BI_count[1]+=2
        j = i - 1

        for j in range(i - 1, -2, -1):
            BI_count[2]+=2
            if arr[j] > temp:
               arr[j + 1] = arr[j]
               BI_count[3]+=1
            else:
                break
        arr[j + 1] = temp
        BI_count[4]+=1
    return arr

arr = [9,8,7,6,5,4]
BI_count=[0,0,0,0,0]
Arr = Insertion_sort(arr)
print(Arr)
print(BI_count)