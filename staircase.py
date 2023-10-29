def staircase(numbers_of_stairs: int) -> None:
    for i in range(numbers_of_stairs):
        print(f"{' '*(numbers_of_stairs - (i+1))}{'#'*(i+1)}")
