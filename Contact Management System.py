import re
import json

# Contact data storage
contacts = {}

# Display menu
def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Backup contacts")
    print("9. Restore contacts")
    print("10. Quit")

# Get menu choice
def get_menu_choice():
    choice = input("Enter your choice (1-10): ")
    return choice

# Add contact
def add_contact(contact_id, name, phone, email, additional_info, categories, custom_fields):
    contacts[contact_id] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info,
        "Categories": categories,
        **custom_fields
    }

# Add new contact
def add_new_contact():
    contact_id = input("Enter contact ID (e.g., phone number or email): ")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (e.g., address, notes): ")
    categories = input("Enter categories (comma-separated): ").split(',')
    custom_fields = {}
    while True:
        field_name = input("Enter custom field name (or 'done' to finish): ")
        if field_name.lower() == 'done':
            break
        field_value = input(f"Enter value for {field_name}: ")
        custom_fields[field_name] = field_value
    add_contact(contact_id, name, phone, email, additional_info, categories, custom_fields)
    print("Contact added successfully!")

# Edit contact
def edit_contact(contact_id):
    if contact_id in contacts:
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        additional_info = input("Enter new additional information: ")
        categories = input("Enter new categories (comma-separated): ").split(',')
        custom_fields = {}
        while True:
            field_name = input("Enter custom field name (or 'done' to finish): ")
            if field_name.lower() == 'done':
                break
            field_value = input(f"Enter value for {field_name}: ")
            custom_fields[field_name] = field_value
        add_contact(contact_id, name, phone, email, additional_info, categories, custom_fields)
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Delete contact
def delete_contact(contact_id):
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Search contact
def search_contact(query):
    results = []
    for contact_id, details in contacts.items():
        if query.lower() in contact_id.lower() or any(query.lower() in value.lower() for value in details.values()):
            results.append((contact_id, details))
    if results:
        for contact_id, details in results:
            print(f"Contact ID: {contact_id}")
            for key, value in details.items():
                print(f"  {key}: {value}")
    else:
        print("No contacts found matching the query.")

# Display all contacts
def display_all_contacts(sort_by="Name"):
    if contacts:
        sorted_contacts = sorted(contacts.items(), key=lambda item: item[1].get(sort_by, ""))
        for contact_id, details in sorted_contacts:
            print(f"Contact ID: {contact_id}")
            for key, value in details.items():
                print(f"  {key}: {value}")
    else:
        print("No contacts available.")

# Export contacts
def export_contacts(filename):
    with open(filename, 'w') as file:
        for contact_id, details in contacts.items():
            file.write(f"Contact ID: {contact_id}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    print("Contacts exported successfully!")

# Import contacts
def import_contacts(filename):
    global contacts
    with open(filename, 'r') as file:
        lines = file.readlines()
        contact_id = None
        for line in lines:
            line = line.strip()
            if line.startswith("Contact ID:"):
                contact_id = line.split(": ")[1]
                contacts[contact_id] = {}
            elif contact_id and line:
                key, value = line.split(": ")
                contacts[contact_id][key] = value
    print("Contacts imported successfully!")

# Backup contacts
def backup_contacts(filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print("Contacts backed up successfully!")

# Restore contacts
def restore_contacts(filename):
    global contacts
    with open(filename, 'r') as file:
        contacts = json.load(file)
    print("Contacts restored successfully!")

# Main function
def main():
    while True:
        display_menu()
        choice = get_menu_choice()
        try:
            if choice == '1':
                add_new_contact()
            elif choice == '2':
                contact_id = input("Enter contact ID to edit: ")
                edit_contact(contact_id)
            elif choice == '3':
                contact_id = input("Enter contact ID to delete: ")
                delete_contact(contact_id)
            elif choice == '4':
                query = input("Enter search query: ")
                search_contact(query)
            elif choice == '5':
                sort_by = input("Enter sorting criteria (Name, Phone, Email, etc.): ")
                display_all_contacts(sort_by)
            elif choice == '6':
                filename = input("Enter filename to export contacts: ")
                export_contacts(filename)
            elif choice == '7':
                filename = input("Enter filename to import contacts: ")
                import_contacts(filename)
            elif choice == '8':
                filename = input("Enter filename to backup contacts: ")
                backup_contacts(filename)
            elif choice == '9':
                filename = input("Enter filename to restore contacts: ")
                restore_contacts(filename)
            elif choice == '10':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
