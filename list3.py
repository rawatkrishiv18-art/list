L = [4,8,9,10,5,3,2,7]
print("The original list is : ",L)

count = 0
for i in L:
    count += i

AVG = count / len(L)

print("sum :",count)
print("average :",AVG)
L.sort()
print("smallest number :",L[0])
print("largest number :",L[-1])