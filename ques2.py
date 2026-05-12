

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lst = list(map(int, input("Enter list elements separated by comma: ").split(',')))


mid_index = len(lst) // 2
mid_value = lst[mid_index]

total_Sum = add(num1, num2)

print("Sum =", total_Sum)
print("Middle value =", mid_value)

if total_Sum > mid_value:
    result = set(lst[:mid_index])
    print("Set:", result)
