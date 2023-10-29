def plusMinus(array: list) -> None:
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0
    array_lenght = len(array)

    for value in array:
        if value > 0:
            positive_numbers += 1
        elif value < 0:
            negative_numbers += 1
        else:
            zeros += 1

    print(f"{positive_numbers/array_lenght:6f}")
    print(f"{negative_numbers/array_lenght:6f}")
    print(f"{zeros/array_lenght:6f}")


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
