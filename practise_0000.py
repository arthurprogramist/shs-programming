list1 = [1, 2, 3, 4, 5]
print(list1)
# print(list1[2])
# print(list1[-3])

list1 += [7, 10, 9]
print(list1)

list1.append([8, 3, 9])
print(list1)

print(list1[8][2])
print(list1[-1][-1])

print(list1[len(list1)-1][2])

print(list1.pop(1))
print(list1)
lst2 = list1.copy()
lst2.reverse()
print(lst2)
print(list1)


print(list1)

print([1, 2] < [3])
print([1, 5] > [4])
print([1, 2] < [3, 1])
print([15, 1] > [3, 2])
print(len([15, 1]) == len([3, 2]))
