
# Event Processing System using Queue

events = []

# 1. Add an Event
def add_event(event):
    events.append(event)
    print("Event added successfully!")

# 2. Process the Next Event
def process_event():
    if events:
        event = events.pop(0)
        print("Processing Event:", event)
    else:
        print("No events to process!")

# 3. Display Pending Events
def display_events():
    if events:
        print("Pending Events:", events)
    else:
        print("No pending events!")

# 4. Cancel an Event
def cancel_event(event):
    if event in events:
        events.remove(event)
        print("Event cancelled successfully!")
    else:
        print("Event not found!")

# Main Menu
while True:
    print("\n1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        event = input("Enter event name: ")
        add_event(event)

    elif choice == 2:
        process_event()

    elif choice == 3:
        display_events()

    elif choice == 4:
        event = input("Enter event to cancel: ")
        cancel_event(event)

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
