# online sorting

def online_sort(lst: list) -> list:
    # This function sorts the resulting list from min to max.
    # The first loop goes from the beginning of the list,
    # if the next value is less than the current one, it is stored
    # in 'mem_value', the current value is entered in its place.
    # In the next loop by iterating from the beginning, mem_value is inserted
    # into the desired position in the already sorted part of the list.
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            mem_value = lst[i+1]
            lst[i+1] = lst[i]
            for j in range(i+1):
                if mem_value >= lst[j]:
                    continue
                else:
                    lst[j], mem_value = mem_value, lst[j]
    return lst
    

def create_list(n: int) -> list:
    lst = []
    while n != 0:
        lst.append(int(input('Enter the nomber: ')))
        n -= 1
    return lst


def main():
    N = int(input('The list lenght should be: '))
    lst = create_list(N)
    print(f'The create list: \n{lst}')
    print(f'The sorted list: \n{online_sort(lst)}')


main()
