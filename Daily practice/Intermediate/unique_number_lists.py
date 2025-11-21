# Define two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Convert to sets and find symmetric difference
unique_elements = list(set(list1) ^ set(list2))

print(unique_elements)  # Output: [1, 2, 5, 6]
