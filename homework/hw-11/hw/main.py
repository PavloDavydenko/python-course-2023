from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass

    def __repr__(self):
        return str(self._value)


class Name(Field):
    pass


class Phone(Field):
    def validate(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Invalid phone number format. It should contain 10 digits.")

    def __repr__(self):
        return f"{super().__repr__()}"


class Birthday(Field):
    def validate(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. It should be YYYY-MM-DD.")

    def __repr__(self):
        return f"Birthday({super().__repr__()})"


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not any(p.value == old_phone for p in self.phones):
            raise ValueError(f"Phone number '{old_phone}' not found for editing.")

        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def days_to_birthday(self):
        if self.birthday and self.birthday.value:
            today = datetime.now().date()
            birthday_date = datetime.strptime(self.birthday.value, "%Y-%m-%d").date()

            next_birthday = datetime(today.year, birthday_date.month, birthday_date.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

            return (next_birthday - today).days

        return None

    def __str__(self):
        return f"Contact name: {self.name.value}; phones: {', '.join(str(p) for p in self.phones)}; " \
               f"birthday: {self.birthday.value}" if self.birthday else "No birthday specified"

    def __repr__(self):
        return f"Record(name={self.name.value}, phones={[repr(p) for p in self.phones]}, birthday={self.birthday.value})"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, batch_size=3):
        records = list(self.data.values())
        for i in range(0, len(records), batch_size):
            yield records[i:i + batch_size]


def main():
    address_book = AddressBook()

    contact1 = Record("John")
    contact1.add_phone("1234567890")
    address_book.add_record(contact1) 

    contact2 = Record("Kate", "1985-07-15")
    contact2.add_phone("9876543210")
    contact2.add_phone("0987654321")
    address_book.add_record(contact2)

    contact3 = Record("Dan", "1980-01-01")
    contact3.add_phone("1111111111")
    contact3.add_phone("1111111115")
    address_book.add_record(contact3)

    contact4 = Record("Smith", "2000-01-01")
    contact4.add_phone("0000000000")
    address_book.add_record(contact4)

    contact5 = Record("Jane", "2005-05-05")
    contact5.add_phone("5555555555")
    contact5.add_phone("1555555555")
    address_book.add_record(contact5)

    contact6 = Record("Jane_2")
    contact6.add_phone("5555555555")
    contact6.add_phone("1555555555")
    address_book.add_record(contact6)

    for name, record in address_book.data.items():
        print(f"{name}: {record}; Days to Birthday: {record.days_to_birthday()}")

    for batch in address_book.iterator():
        print("\nNext batch of records:")
        for record in batch:
            print(record)


if __name__ == "__main__":
    main()
