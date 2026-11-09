import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")


def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contacts(contacts):
    term = input("Enter name to search: ").strip().lower()
    matches = [c for c in contacts if term in c['name'].lower()]
    if not matches:
        print("No matching contacts found.")
        return
    for c in matches:
        print(f"{c['name']} | {c['phone']} | {c['email']}")


def edit_contact(contacts):
    term = input("Enter contact name to edit: ").strip().lower()
    for c in contacts:
        if term in c['name'].lower():
            new_name = input(f"Name ({c['name']}): ").strip()
            new_phone = input(f"Phone ({c['phone']}): ").strip()
            new_email = input(f"Email ({c['email']}): ").strip()
            if new_name: c['name'] = new_name
            if new_phone: c['phone'] = new_phone
            if new_email: c['email'] = new_email
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")


def delete_contact(contacts):
    term = input("Enter contact name to delete: ").strip().lower()
    for c in contacts:
        if term in c['name'].lower():
            contacts.remove(c)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")


def main():
    contacts = load_contacts()
    while True:
        print("
===== Contact Book =====")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print('Invalid option.')

if __name__ == '__main__':
    main()
