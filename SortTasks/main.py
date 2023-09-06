array = [8, -4, 9, 1, 5]

for i, num in enumerate(array):
    mem_value = 0
    if i == len(array) - 2:
        break
    elif num > array[i+1]:
        mem_value = array[i+1]
        array[i+1] = num
        for j in range(i, -1, -1):
            if array[j-1] > mem_value:
                array[j] = array[j+1]
            else:
                array[j] = mem_value



print(array)
