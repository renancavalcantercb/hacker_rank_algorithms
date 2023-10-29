def diagonalDifference(array: list) -> int:
    array_lenght = len(array)
    left_diagonal = sum(array[i][i] for i in range(array_lenght))
    right_diagonal = sum(array[i][array_lenght - i - 1] for i in range(array_lenght))
    return abs(left_diagonal - right_diagonal)
