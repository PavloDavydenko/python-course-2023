from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if not (self.value.isdigit() and len(self.value) == 10):
            raise ValueError(
                "Invalid phone number format. It should contain 10 digits."
                )


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not any(p.value == old_phone for p in self.phones):
            raise ValueError(
                f"Phone number '{old_phone}' not found for editing."
                )

        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {
            '; '.join(str(p) for p in self.phones)
            }"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


def main():
    address_book = AddressBook()

    while True:
        command = input(
            "Enter command ('add', 'change', 'find', 'delete', "
            "'exit' or '.'): "
            )

        if command == "exit" or command == "quit" or command == ".":
            print("Exiting the program.")
            break

        if command == "add":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")

            contact = Record(name)
            contact.add_phone(phone)
            address_book.add_record(contact)
            print(f"Contact '{name}' added successfully.")

        elif command == "change":
            name = input("Enter the name for the change: ")
            new_phone = input("Enter the new phone number: ")

            found_contact = address_book.find(name)
            if found_contact:
                old_phone = input("Enter the old phone number to change: ")
                try:
                    found_contact.edit_phone(old_phone, new_phone)
                    print(
                        f"Phone number changed successfully for cantact '{name}'."
                        )
                except ValueError as e:
                    print(f"Error: {e}")

        elif command == "find":
            name = input("Enter the name to find: ")
            found_contact = address_book.find(name)

            if found_contact:
                print(found_contact)
            else:
                print(f"Contact '{name}' not found.")

        elif command == "delete":
            name = input("Enter the name to delete: ")
            address_book.delete(name)
            print(f"Contact '{name}' deleted successfully.")

        else:
            print(
                "Invalid command. Please enter 'add', 'change', "
                "'find', 'delete', 'exit' or '.'."
                )


if __name__ == "__main__":
    main()
