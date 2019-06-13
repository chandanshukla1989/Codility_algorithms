def solution(A, B, F):
    arr=[];
    if(len(A)!=len(B)):
        return 0
    if(F>len(A)):
        return 0
    if(len(A)>200000):
        return 0
    if(A[0]>=1000):
        return 0;
  
    if(len(A)==0):
        return 0;
    if(len(A)==F):
        return sum(A)
    if(F==0):
        return sum(B)

   
        
    
    #print(max(A[0]+solution(A[1:],B[1:],F-1),B[0]+solution(A[1:],B[1:],F)))

    return max(A[0]+solution(A[1:],B[1:],F-1),B[0]+solution(A[1:],B[1:],F))
    # write your code in Python 3.6
pass

def max(a,b):
    if(a>=b):
        return a
    else:
        return b
def sum(A):
    sum=0
    for item in A:
        sum+=item
    return sum
