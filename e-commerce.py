
# Program to search customer account IDs

# List of customer account IDs
account_ids = [105, 102, 108, 101, 106, 103, 107]

# ID to be searched
search_id = int(input("Enter customer account ID to search: "))

# 1. Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

result = linear_search(account_ids, search_id)

if result != -1:
    print("Linear Search: Account ID found at position", result + 1)
else:
    print("Linear Search: Account ID not found")

# 2. Binary Search
# Binary search requires a sorted list
sorted_ids = sorted(account_ids)

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

result = binary_search(sorted_ids, search_id)

if result != -1:
    print("Binary Search: Account ID found at position", result + 1)
else:
    print("Binary Search: Account ID not found")
