
borrow_count = [5, 0, 3, 8, 2, 0, 5, 1, 8, 4]

n = len(borrow_count)

# 1. Calculate average number of books borrowed
total = sum(borrow_count)
average = total / n
print("Average books borrowed:", average)

# 2. Find highest and lowest borrowings
highest = max(borrow_count)
lowest = min(borrow_count)

print("Highest borrow count:", highest)
print("Lowest borrow count:", lowest)

# 3. Count members who borrowed zero books
zero_count = borrow_count.count(0)
print("Members who borrowed no books:", zero_count)

# 4. Find mode (most frequent borrow count)
frequency = {}

for count in borrow_count:
    frequency[count] = frequency.get(count, 0) + 1

max_frequency = max(frequency.values())

modes = [key for key, value in frequency.items()
         if value == max_frequency]

print("Most frequently occurring borrow count:", modes)
print("Frequency:", max_frequency)
