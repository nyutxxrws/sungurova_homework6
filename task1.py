def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)
assert average_num([1, 1]) == 1
assert average_num([2.5, 3.5]) == 3
assert average_num([10, 20, 30, 40]) == 25
assert average_num([1, 2, 3, 4, 5]) == 3
assert average_num([0.5, 1.5, 2.5]) == 1.5
assert average_num([-5, 0, 5]) == 0
assert average_num([100]) == 100
assert average_num([1.1, 2.2, 3.3]) == 2.2
assert average_num([4, 4, 4, 4]) == 4
assert average_num([2, 4, 6, 8, 10]) == 6
print("Все 10 тестов пройдены успешно!")