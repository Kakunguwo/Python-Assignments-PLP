# Initialize an empty list
my_list = []

# Append integers to the list
my_list.append(10)  # List becomes [10]
my_list.append(20)  # List becomes [10, 20]
my_list.append(30)  # List becomes [10, 20, 30]
my_list.append(40)  # List becomes [10, 20, 30, 40]

# Insert the integer 15 at index 1 which is position 2
my_list.insert(1, 15)  # List becomes [10, 15, 20, 30, 40]

# Extend the list by adding multiple integers at once
my_list.extend([50, 60, 70])  # List becomes [10, 15, 20, 30, 40, 50, 60, 70]

# Print the current state of the list
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element from the list
my_list.pop()  # List becomes [10, 15, 20, 30, 40, 50, 60]

# Print the current state of the list after popping
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

# Sort the list in ascending order
my_list.sort()  # List becomes [10, 15, 20, 30, 40, 50, 60]

# Find the index of the element 30 in the list
index0f30 = my_list.index(30)  # index0f30 will be 3

# Print the index of the element 30
print(index0f30)  # Output: 3

# Print the final state of the list
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]