def compareTriplets(a: list, b: list) -> list:
    result_list = [0, 0]
    for index in range(len(a)):
        if a[index] > b[index]:
            result_list[0] += 1
        elif a[index] < b[index]:
            result_list[1] += 1

    return result_list
