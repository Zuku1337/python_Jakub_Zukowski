def check_number_in_list(numbersMatrix: list, number: int) -> bool:
    if number in numbersMatrix:
        return True
    return False


print(check_number_in_list([1,2,3,4], 3))