#given a list of numbers find how many of them are positive and how many of them are negative.

numbers = [5, -2, 10, -7, 3, -1]

i = 0
positive = 0
negative = 0

while i < len(numbers):
    if numbers[i] > 0:
        positive = positive + 1
    if numbers[i] < 0:
        negative = negative + 1
    i = i + 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
