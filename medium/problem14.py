nums = [1,2,3]

def permute(nums):
    ls1=[]
    length=len(nums)
    def per(ls):
        if len(ls)==length:
            ls1.append(ls)
            return

        for i in nums:
            if i not in ls:
                per(ls+[i])

    per([])
    return ls1
print(permute(nums))