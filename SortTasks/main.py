array = [8, -4, 9, 1, 5, 3, 7, 2, -3, 4]

mem_value = array[0]

for i, num in enumerate(array):
    if i == len(array) - 2:
        break
    elif num > array[i+1]:
        mem_value = array[i+1]
        array[i+1] = num
        if i == 0:
            array[i] = mem_value
        for j in range(i, 0, -1):
            if array[j-1] > mem_value:
                array[j] = array[j-1]
            else:
                array[j] = mem_value
                break

print(array)
