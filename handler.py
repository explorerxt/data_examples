import json

def load_data():
    with open('data.json') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_data():
    data = load_data()
    id = int(input("Enter the ID: "))
    name = input("Enter the name: ")
    surname = input("Enter the surname: ")
    points_earned = int(input("Enter the points earned: "))
    new_entry = {
        'id': id,
        'name': name,
        'surname': surname,
        'points_earned': points_earned
    }
    data.append(new_entry)
    save_data(data)
    print("Data added successfully.")

def remove_data():
    data = load_data()
    id = int(input("Enter the ID of the data entry to remove: "))
    for entry in data:
        if entry['id'] == id:
            data.remove(entry)
            save_data(data)
            print("Data removed successfully.")
            return
    print("No data entry found with the provided ID.")

# Main program loop
while True:
    print("--- Data Management ---")
    print("1. Add Data")
    print("2. Remove Data")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_data()
    elif choice == '2':
        remove_data()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
