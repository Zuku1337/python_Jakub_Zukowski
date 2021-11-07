def get_numbers(matrix):
    value = 0
    for number in matrix:
        value += number * 2
    return value


def output_numbers():
    value = 0
    for number in range(1, 6):
        value += number * 2
    return value


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(get_numbers(numbers))
    print(output_numbers())

