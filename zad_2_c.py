if __name__ == '__main__':
    numbers = [i for i in range(10)]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print(i)
