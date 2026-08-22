s = input()
count = 0
n = len(s)
for ind in range(0,n-1):
    if(s[ind].islower() and s[ind+1].isupper() or s[ind].isupper() and s[ind+1].islower()):
        count =+ 1
print(count)
