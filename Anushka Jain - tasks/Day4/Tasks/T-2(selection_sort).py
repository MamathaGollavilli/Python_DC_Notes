#selection sort
li = [5, 4, 3, 2, 1]
n = len(li)
for i in range(0, n):
    minimum = i
    for j in range(i+1, n):
        if(li[j] < li[minimum]):
            minimum = j
    li[i], li[minimum] = li[minimum], li[i]
print(li)
            
        
