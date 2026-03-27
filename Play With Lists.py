L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list:", L)
count = 0
for i in L:
    count += 1

avg = count/len(L)

print("sum = ", avg)
print("Average = ", avg)

L.sort()

print("the smallest ellement is:", L[0])
print("the largest ellement is:", L[-1])