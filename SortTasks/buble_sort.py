# buble sorting

def sort_list(lst: list) -> list:
    for i in range(len(lst)-1):
        for j in range(len(lst) - i - 1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
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
    print(f'The sorted list: \n{sort_list(lst)}')


main()
