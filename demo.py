for it in range(1, 10):
    print(it)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

for x in range(4):
    for y in range(3):
        print(f'{x},{y}')

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print("*" * i)

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    output = ""
    for count in range(i):
        output += "X"
    print(output)

number = [1, 2, 8, 3, 4, 5, 6]
print(max(number))

number = [1, 2, 9, 3, 4, 5, 6]
ma = number[0]
for num in number:
    if num > ma:
        ma = num
print(ma)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])
for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = number.copy()
numbers.append(10)
def remove(numbers2):
    pass
print(numbers2)

numb = [2, 2, 4, 6, 3, 4, 6, 1]
uni = []
for nu in numb:
    if nu not in uni:
        uni.append(nu)
print(uni)