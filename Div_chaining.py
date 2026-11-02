
# Hash Table using Division Method and Chaining

SIZE = 10

# Create an empty hash table
hash_table = [[] for _ in range(SIZE)]

# Hash Function
def hash_function(key):
    return key % SIZE

# Insert Operation
def insert(key, value):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Key updated successfully!")
            return

    hash_table[index].append([key, value])
    print("Key inserted successfully!")

# Search Operation
def search(key):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            print("Value found:", pair[1])
            return

    print("Key not found!")

# Delete Operation
def delete(key):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print("Key deleted successfully!")
            return

    print("Key not found!")

# Display Hash Table
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])


# Main Menu
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
