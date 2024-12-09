L =[4,6,8,7,1,9,2,3]

count = 0
for i in L:
    count += i

avg = count / len(L)
#print(avg)

L.sort()

print(L)

print(L[0])
print(L[-1])