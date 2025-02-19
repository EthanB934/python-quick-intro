# Initialize an empty phonebook
phonebook = {}

# Function to add a contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added with number {number}.")

# Function to remove a contact
def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' removed.")
    else:
        print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    print("Phonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

# Adding contacts
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
add_contact("Charlie", "555-555-5555")

# Displaying contacts
display_contacts()

# Removing a contact
remove_contact("Bob")

# Displaying contacts again
display_contacts()

# View the entire dictionary
print(phonebook)