#take 5 numbers store them in a list. print the list in reverse order

List = [1, 2, 3, 4, 5]

# Print the list in reverse order without using reverse() function
for i in range(len(List) - 1, -1, -1):
    print(List[i], end=' ')
print()  # For a new line at the end