def check_number_in_list(numbers_matrix: list, number: int) -> bool:
    if number in numbers_matrix:
        return True
    return False


print(check_number_in_list([1,2,3,4], 3))
