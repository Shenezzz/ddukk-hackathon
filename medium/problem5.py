nums=[100,4,200,1,3,2]

def longest_sequence(nums):
    n=set(nums)
    maxx=0
    for i in n:
        
        if i-1 not in n:
            count=1
            num1=i
            while(True):
                num1+=1
                if num1 in n:
                    count+=1
                maxx=max(count,maxx)
                if num1 not in n:
                    break

    return maxx
print(longest_sequence(nums))

