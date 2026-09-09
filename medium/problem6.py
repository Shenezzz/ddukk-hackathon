height = [1,1]


def most_water(height):
    maxx=0
    length=len(height)
    for i in range(length):
        for j in range(i+1,length):
            maxx=max(maxx,(j-i)*min(height[i],height[j]))

    return maxx

print(most_water(height))