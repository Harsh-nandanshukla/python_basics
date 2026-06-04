def max_consecutive(nums):
    cnt=0
    maxn=0
    for i in range(len(nums)):
        if nums[i]==1:
            cnt=cnt+1
            maxn=max(maxn,cnt)
        else:
            cnt=0
    return maxn

print(max_consecutive([1,1,0,1,1,1,0,1]))            