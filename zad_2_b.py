def get_numbers_with_array(matrix):
    new_matrix = []
    for i in matrix:
        new_matrix.append(i * 2)
    return new_matrix


def get_numbers_with_list(matrix):
    return [i * 2 for i in matrix]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(get_numbers_with_array(numbers))
    print(get_numbers_with_list(numbers))
