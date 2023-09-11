def solution(a: list[int]) -> int:
    east_cars = 0
    passing_cars = 0
    for car in a:
        if car == 0:
            east_cars += 1
        else:
            passing_cars += east_cars
    return passing_cars