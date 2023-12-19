def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Enter name and phone"
        except IndexError:
            return "Contact not found"
    return wrapper


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f'Contact "{name}" added successfully.'


@input_error
def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f'Phone number for "{name}" changed successfully.'
    else:
        raise IndexError


@input_error
def show_phone(name):
    if name in contacts:
        return f'The phone number for "{name}" is "{contacts[name]}".'
    else:
        raise IndexError


def show_all_contacts():
    if not contacts:
        return "No contacts found"
    else:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name: <20}: {phone}\n"

        return result


def exit():
    return "Good bye!"


def handle_command_hello():
    return "How can I help you?"


def handle_command_add(data):
    if len(data) == 2:
        return add_contact(*data)
    else:
        raise ValueError


def handle_command_change(data):
    if len(data) == 2:
        return change_contact(*data)
    else:
        raise ValueError


def handle_command_phone(data):
    if len(data) == 1:
        return show_phone(*data)
    else:
        raise ValueError


COMMANDS_DICT = {
        "add": handle_command_add,
        "change": handle_command_change,
        "phone": handle_command_phone,
        "hello": handle_command_hello,
        "show all": show_all_contacts,
        "good bye": exit,
        "close": exit,
        "exit": exit,
        ".": exit,
    }


def handle_command(user_input):
    command = ''
    data = ''

    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            command = key
            data = user_input[len(command):]
            break

    if not command:
        return "Invalid command. Type 'hello' for assistance."

    if data:
        data = data.strip().split(" ")
        return COMMANDS_DICT[command](data)
    return COMMANDS_DICT[command]()


def main():
    while True:
        user_input = input("Enter your command: ")
        result = handle_command(user_input)
        print(result)

        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
