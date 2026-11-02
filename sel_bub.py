
# Program to sort employee salaries

salaries = [45000.50, 65000.75, 30000.25, 85000.00,
            55000.50, 95000.25, 40000.00, 75000.80]

# 1. Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 2. Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Selection Sort
selection_result = selection_sort(salaries.copy())
print("Selection Sort:", selection_result)
print("Top 5 Highest Salaries:", selection_result[-5:][::-1])

# Bubble Sort
bubble_result = bubble_sort(salaries.copy())
print("\nBubble Sort:", bubble_result)
print("Top 5 Highest Salaries:", bubble_result[-5:][::-1])
