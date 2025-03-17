m,n,x = list(map(int,input().strip().split()))
a = sorted(list(map(int,input().strip().split())))
b = sorted(list(map(int,input().strip().split())))
j = 0
count = 0
for i in a:
    if j>=len(b): break
    if b[j]-x>i: continue
    while j<len(b) and b[j]+x<i:
        j+=1
    if j<n and b[j]-x<=i and i<=b[j]+x:
        count+=1
        j+=1
print(count)

