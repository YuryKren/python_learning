# online sorting

from random import randint

array = []
lght = 100
while lght != 0:
    array.append(randint(-100, 1000))
    lght -= 1

print(array)


for i in range(len(array)-1):
    if array[i] > array[i+1]:
        mem_value = array[i+1]
        array[i+1] = array[i]
        for j in range(i+1):
            if mem_value >= array[j]:
                continue
            else:
                array[j], mem_value = mem_value, array[j]
    

print(array)
