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


def handle_command_add(parts):
    if len(parts) == 2:
        return add_contact(*parts[1].split())
    else:
        raise ValueError


def handle_command_change(parts):
    if len(parts) == 2:
        return change_contact(*parts[1].split())
    else:
        raise ValueError


def handle_command_phone(parts):
    if len(parts) == 2:
        return show_phone(parts[1])
    else:
        raise ValueError


def handle_command(command):
    parts = command.split(" ", 1)
    # print(parts)
    action = parts[0].lower()
    # print(action)
    act_command = command.lower()

    commands = {
        "hello": handle_command_hello,
        "show all": show_all_contacts,
        "good bye": exit,
        "close": exit,
        "exit": exit,
        ".": exit,
    }

    arg_commands = {
        "add": handle_command_add,
        "change": handle_command_change,
        "phone": handle_command_phone,
    }

    if action in commands:
        return commands[action]()
    elif action in arg_commands:
        return arg_commands[action](parts)
    elif act_command in commands:
        return commands[act_command]()
    else:
        return "Invalid command. Type 'hello' for assistance."


def main():
    while True:
        user_input = input("Enter your command: ")
        result = handle_command(user_input)
        print(result)

        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()