from sortedcontainers import SortedList


m,n = list(map(int,input().strip().split()))
a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))
a_ = SortedList()

for i in a: a_.add(i)

for i in b:
    if not a_: 
        print(-1)
        continue
    index = a_.bisect_left(i)
    if index==0: 
        if a_[index]!=i:
            print(-1)
        else: 
            print(a_[0])
            a_.pop(0)
    else:
        if index==len(a_) and len(a_)>0: 
            print(a_[-1])
            a_.pop(-1) 
        elif a_[index]==i: 
            print(i)
            a_.pop(index)
        else:
            print(a_[index-1] if index>0 else -1)
            a_.pop(index-1)
    
        
    