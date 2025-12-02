#import numpy as np
def fib_iterative(n):
    a,b=0,1
   
    for _ in range(n):
       a,b=b,a+b
    return a
    
print(fib_iterative(6))



'''
def fib(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))


def mainfib(n):
    def mat_paw(M,p):
        if p==1:
            return M
        if p%2==0:
           half= mat_paw(M,p//2)
           return np.dot(half,half)
        else:
           return np.dot(M,mat_paw(M,p-1)) 

    if n==0:
        return 0
    F=np.array([[1,1],[1,0]])
    result=mat_paw(F,n-1)
    return result[0][0]
print(mainfib(6))'''