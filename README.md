# Contact Book

A simple menu-driven Contact Book application built using Python. This application allows users to store and manage contact information. All contact data is saved in a JSON file, which means the data remains available even after closing and restarting the program.

## Features

- Add new contacts
- View all saved contacts
- Search contacts using partial name matching
- Edit existing contacts
- Delete contacts
- Store contact information in a JSON file
- Automatically load saved contacts when the program starts
- Start with an empty contact list if the JSON file is missing or corrupted

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions

## Project Structure

```
contact-book/
│
├── contact_book.py
├── contacts.json
└── README.md
```

## Contact Information

Each contact contains the following details:

- Name
- Phone Number
- Email Address

Example:

```json
{
    "name": "John Smith",
    "phone": "9876543210",
    "email": "john@example.com"
}
```

## How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/contact-book.git
```

### Open the Project Folder

```bash
cd contact-book
```

### Run the Program

```bash
python contact_book.py
```

## Menu Options

When the program starts, the following menu will be displayed:

```text
1. Add Contact
2. List Contacts
3. Search Contacts
4. Edit Contact
5. Delete Contact
6. Exit
```

## Error Handling

The application handles common errors gracefully:

- If `contacts.json` does not exist, an empty contact list is created.
- If the JSON file contains invalid data, the application starts with an empty contact list instead of crashing.

## Design Decisions

- JSON was used because it is lightweight, simple, and easy to read.
- Partial name matching was implemented to improve search functionality.
- Contact data is saved immediately after adding, editing, or deleting a contact so that no information is lost.

## Future Improvements

Possible future enhancements include:

- Contact sorting
- Input validation
- Multiple phone numbers per contact
- Export contacts to CSV
- Contact categories
