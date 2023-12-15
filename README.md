# Personal Assistant CLI Application

This is a command-line interface (CLI) application for managing an address book. The application allows you to add, edit, and view contacts along with their phone numbers and birthdays, email, and home addresses. Allows search for address book with matches in phone, name or other fields.

Module Notes allows working with notes, creating, deleting, and sorting them. Keyword search functionality has been implemented.

Module SortFolder will sort your files in the target folder, depends file extension for categories: Images, Video, Documents, Archives etc. After sorting, archives will be unpacked, and Cyrillic symbols translate to Latin

## Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/kondrat1206/Project-group7.git
   ```

   ```bash
   cd ./Project-group7
   ```

2. Build packet:

   Update setuptools и wheel version:

   ```bash
   pip install --upgrade setuptools wheel
   ```

   Build:

   ```bash
   python setup.py sdist bdist_wheel
   ```

3. Install packet to the system:

   ```bash
   pip install ./dist/assistant-0.1.0-py3-none-any.whl
   ```

4. Run the application:

   ```bash
   assistant
   ```

## Available Commands:

- **hello**: Print "How can I help you?"

- **add contact [name] [phone] [birthday]**: Add a new record to the address book or a new phone. Provide the contact's name , and an optional phone number and birthday in the format 'DD.MM.YYYY'.

- **add birthday [name] [birthday]**: Add a new or change the birthday of a contact in the address book. Provide the contact's name and the birthday in the format 'DD.MM.YYYY'.

- **add email [name] [email]**: Add email to the contact of address book.

- **add address [name] [address]**: Add address to the contact of address book.

- **change phone [name] [old_phone] [new_phone]**: Change phone num for contact in address book.

- **change email [name] [new email]**: Change email for contact in address book.

- **change address [name] [new address]**: Change address for contact in address book.

- **remove [name]**: Delete a contact from the address book. Provide the contact's name to be removed.

- **phone [name]**: Show the phone list of a contact.

- **show all**: Show the entire address book.

- **pages [size]**: Show the address book in pages, where the size is the number of records per page.

- **to birthday [name]**: Show the number of days until the contact's birthday.

- **celebrators [days to celebrate]**: Show users with birthday less then set days

- **search [string]**: Perform a matching search for a name or phone number in the address book.

- **sort folder [path to folder]**: Sort files depends extensions into the target folder

- **notes**: module for user notes

- **good bye, close, exit**: Print "Good bye!" and exit the application.

- **help**: Show this help message.

## Usage:

1. Run the application by executing the script.

2. Enter commands as described above.

3. Type 'exit' to end the application.

Enjoy managing your address book through the command line!
