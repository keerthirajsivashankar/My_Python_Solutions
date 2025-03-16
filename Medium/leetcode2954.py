def repairCars(ranks: list[int], cars: int) -> int:
    def is_feasible(time: int) -> bool:
        repaired_cars = 0
        for rank in ranks:
            repaired_cars += int((time / rank) ** 0.5)
        return repaired_cars >= cars

    left = 0
    right = max(ranks) * cars * cars
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if is_feasible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

# Driver Code
if __name__ == "__main__":
    ranks1 = [4, 2]
    cars1 = 10
    result1 = repairCars(ranks1, cars1)
    print(f"Minimum time for {ranks1}, {cars1}: {result1}")

    ranks2 = [1, 2, 3, 4]
    cars2 = 100
    result2 = repairCars(ranks2, cars2)
    print(f"Minimum time for {ranks2}, {cars2}: {result2}")

    ranks3 = [5,1,8]
    cars3 = 6
    result3 = repairCars(ranks3, cars3)
    print(f"Minimum time for {ranks3}, {cars3}: {result3}")

    ranks4 = [1]
    cars4 = 1000
    result4 = repairCars(ranks4, cars4)
    print(f"Minimum time for {ranks4}, {cars4}: {result4}")