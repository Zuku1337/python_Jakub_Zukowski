def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


isEven = is_even(8)
if isEven:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")