def redandblack(colors , k):
    n  = len(colors)
    extended_colors = colors + colors
    count = 0
    current_length = 1
    for i in range(1,len(extended_colors)):
        if extended_colors[i] != extended_colors[i-1]:
            current_length += 1
        else:
            current_length = 1
        if current_length >= k and i < 2 * n and i >= n :
            count += 1
    return count
#driver code 
colors = list(map(int,input("Enter the list : ").split()))
k = int(input("Ente rthe k : "))
print(redandblack(colors,k))
    