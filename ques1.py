

import statistics as s

def matrix(lst):
    lst += [None] * (9 - len(lst))
    return [lst[i:i+3] for i in range(0, 9, 3)]

def stats(lst):
    t = tuple(lst)
    return {
        "tuple": t,
        "mean": s.mean(lst),
        "median": s.median(lst),
        "mode": s.mode(lst)
    }


def final_result(lst):
    return {
        "matrix": matrix(list.copy()),
        "statistics": stats(lst)
    }

lst = list(map(int, input("Enter numbers: ").split()))

print(final_result(lst))
