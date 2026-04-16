"""
Bubble sort implementation.

This module provides a simple bubble sort algorithm and utilities to create and sort lists.
"""


def sort_list(numbers: list) -> list:
    """
    Sort a list in ascending order using bubble sort algorithm.

    Args:
        numbers: The list of numbers to sort.

    Returns:
        The sorted list.
    """
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def create_list(length: int) -> list:
    """
    Create a list of integers by prompting the user for input.

    Args:
        length: The number of elements to add to the list.

    Returns:
        A list of integers entered by the user.
    """
    numbers = []
    while length != 0:
        numbers.append(int(input('Enter the number: ')))
        length -= 1
    return numbers


def main():
    """
    Main function to demonstrate bubble sort.
    Prompts the user for list length, creates the list, and prints sorted result.
    """
    length = int(input('The list length should be: '))
    numbers = create_list(length)
    print(f'The created list: \n{numbers}')
    print(f'The sorted list: \n{sort_list(numbers)}')


if __name__ == "__main__":
    main()
