nums=list(map(int,input().split()))
target=int(input())
numMap={}
for i,n in enumerate(nums):
    diff=target-n
    if diff in numMap:
        res=[numMap[diff],i]
        print(res)
    numMap[n]=i
