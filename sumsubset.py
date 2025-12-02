def sumsubset(subset,i,currentsum):
    global a,T,n
    if(currentsum==T):
        print(subset)
        return

    for j in range(i,n):
        if(currentsum + a[j]<=T):
            subset.append(a[j])
            sumsubset(subset,j+1,currentsum+a[j])
            subset.pop()

a=[4,2,3,5,7,13,23]
n=len(a)
T=12
print('sumof subsets are:',T,'are')
sumsubset([],0,0)


        