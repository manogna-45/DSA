def robbery(n,s,m):
    avg_security = sum(s) // n 
    robb = []
    for ind in range(0,n):
        if(s[ind] < avg_security):
            robb.append(m[ind])
    return max(robb)
n = int(input())
s = list(map(int,input().split()))
m = list(map(int,input().split()))
print(robbery(n,s,m))
