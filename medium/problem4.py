from collections import Counter

strs = ["eat","tea","tan","ate","nat","bat"]


def group(strs):
    dict1={}
    for i in strs:
        key="".join(sorted(i))
        if key not in dict1:
            dict1[key]=[i]
            continue
        dict1[key].append(i)
    return [val for key,val in dict1.items()]
print(group(strs))


