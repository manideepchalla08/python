def getminsquares(n):
    if n<=3:
        return n;
    res=n
    for i in range(1,n+1):
        temp=i*i;
        if temp>n:
            break
        else:
            res=min(res,1+getminsquares(n-temp))
    return res
n=int(input("enter the number="))
print(getminsquares(n))
