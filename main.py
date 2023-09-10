# merge sorted lists

array = []
array_1 = [2, 4, 7, 9, 12, 15, 16, 21, 23, 25]
array_2 = [1, 4, 5, 11, 17, 18, 20]

print(array_1, f'\n{array_2}')

if len(array_1) >= len(array_2):
    lght = len(array_2)
else:
    lght = len(array_1)


for i in range(lght):
    if array_1[i] <= array_2[i]:
        array.append(array_1[i])
        array.append(array_2[i])
    else:
        array.append(array_2[i])
        array.append(array_1[i])
else:
    if len(array_1) > len(array_2):
        array.extend(array_1[i+1:])
    elif len(array_1) < len(array_2):
        array.extend(array_2[i+1:])

print(array)
