#given a list of marks, count how many students scored
#above 75
#below 40

#using for loop

print("Using for loop:-")


marks = [40, 55, 30, 25, 90, 85, 60]

above_75 = 0
below_40 = 0

for m in marks:
    if m > 75:
        above_75 += 1
    if m < 40:
        below_40 += 1

print("Students scoring above 75:", above_75)
print("Students scoring below 40:", below_40)

#using while loop

print("Using while loop:-")

marks = [40, 55, 30, 25, 90, 85, 60]

i = 0
a = 0   # above 75
b = 0   # below 40

while len(marks) :
    if marks[i] > 75:
        a = a + 1
    if marks[i] < 40:
        b = b + 1
    i = i + 1

print("Students scoring above 75:", a)
print("Students scoring below 40:", b)


