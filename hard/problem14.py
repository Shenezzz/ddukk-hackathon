nums = [3,4,-1,1]


def missing_pos(nums):
    setnums=set(nums)
    n=1
    while(True):
        if n not in setnums:
            return n
        n=n+1

    



print(missing_pos(nums))