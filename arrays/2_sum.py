def two_sum(target,nums):
    mp={}
    for i,num in enumerate(nums):
        b=target-num
        if b in mp:
            return [mp[b],i]
        mp[num]=i

print(two_sum(9,[2,5,7,8]))