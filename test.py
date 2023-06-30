n = int(input("enter the list length"))

array1 = []
for i in range(n):
    array1.append(int(input("enter the value")))

print("list of number ",array1)
max1 = 0
min1 = 1000
for i in range(n):
    if max1 < array1[i]:
        max1 = array1[i]
    if min1 > array1[i]:
        min1 = array1[i]

for i in range(n):
    if array1[i] == max1:
        array1[i] = min1-1

max2 = 0
for i in range(n):
    if max2 < array1[i]:
        max2 = array1[i]

print("second largest value", max2)
    
