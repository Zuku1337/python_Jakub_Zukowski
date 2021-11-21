def matrix_builder(first_matrix: list, second_matrix: list) -> list:
    clear_duplicates = list(set(first_matrix + second_matrix))
    final_matrix = [i ** 3 for i in clear_duplicates]
    return final_matrix


print(matrix_builder([1, 2, 3], [3, 2, 1, 4, 5]))
