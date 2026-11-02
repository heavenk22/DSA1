
# Undo and Redo System using Stack

document = ""
undo_stack = []
redo_stack = []

# Make a Change
def make_change(new_text):
    global document

    undo_stack.append(document)
    document += new_text
    redo_stack.clear()

    print("Change made successfully!")
    display_document()

# Undo Action
def undo():
    global document

    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
        print("Undo successful!")
    else:
        print("Nothing to undo!")

    display_document()

# Redo Action
def redo():
    global document

    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
        print("Redo successful!")
    else:
        print("Nothing to redo!")

    display_document()

# Display Document
def display_document():
    print("Current Document:", document)


# Main Menu
while True:
    print("\n1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter text to add: ")
        make_change(text)

    elif choice == 2:
        undo()

    elif choice == 3:
        redo()

    elif choice == 4:
        display_document()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
