nums = [1,2,3]
k = 3

def subarraysumk(nums,k):
    summ=0
    left=0
    count=0
    for right in range(len(nums)):
        summ+=nums[right]
        while(summ>k):
            summ-=nums[left]
            left+=1

        if summ==k:
            count+=1
    return count
print(subarraysumk(nums,k))