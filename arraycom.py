
#find the maximum value in array

arr=[12,7,8,9,0]
max_value=arr[0]
for i in range(len(arr)):
    if arr[i]>max_value:
        max_value=arr[i]
print("maximum value in the array is", max_value)

#find the second maximum in array

import math
arr=[12,7,8,9,0]

firstmax= math.inf
secondmax= math.inf

for curValue in arr:
    if curValue>firstmax:
        secondmax=firstmax
        firstmax=curValue

    elif curValue>secondmax:
        curValue=secondmax

print("second maximum value in array is", secondmax)