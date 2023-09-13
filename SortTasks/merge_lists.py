# merge sorted lists

result = []
array_1 = [2, 4, 7, 9, 12, 15, 16, 21, 23, 25]
array_2 = [1, 4, 5, 11, 17, 18, 20]

print(array_1, f'\n{array_2}')

i = 0
j = 0

while i < len(array_1) and j < len(array_2):
    if array_1[i] < array_2[j]:
        result.append(array_1[i])
        i += 1
    else:
        result.append(array_2[j])
        j += 1

result.extend(array_1[i:])
result.extend(array_2[j:])

print(result)