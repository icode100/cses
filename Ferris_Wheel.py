n,x = list(map(int,input().strip().split()))
a = sorted(map(int,input().strip().split()))
count = 0
current = 0
ans = 0
i,j = 0,n-1
while i<=j:
    if a[i]+a[j]<=x:
        i+=1
        j-=1
        ans+=1
    else:
        j-=1
        ans+=1
print(ans)
