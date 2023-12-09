class NotEnoughValuesToUnpack(Exception):
    pass


class DictAreEmpty(Exception):
    pass


class ContactIsNotExists(Exception):
    pass


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        if len(args) < 2:
            raise NotEnoughValuesToUnpack

        name, phone = args
        normalized_name = name.capitalize()

        if normalized_name in contacts:
            return "A contact with the same name exists. Please enter a different contact name."

        contacts[normalized_name] = phone
        return "Contact added."
    except NotEnoughValuesToUnpack:
        return 'Name and phone number are required'


def change_contact(args, contacts):
    try:
        if len(args) < 2:
            raise NotEnoughValuesToUnpack

        name, phone = args
        if name not in contacts:
            raise ContactIsNotExists

        if name in contacts:
            contacts[name] = phone
        return "Contact changed."
    except NotEnoughValuesToUnpack:
        return 'Name and phone number are required'
    except ContactIsNotExists:
        return 'Contact with this name not found.'


def get_phone_number(args, contacts):
    try:
        if len(args) < 1:
            raise NotEnoughValuesToUnpack

        if len(contacts) == 0:
            raise DictAreEmpty

        name, = args

        if name not in contacts:
            raise ContactIsNotExists

        return contacts[name]

    except NotEnoughValuesToUnpack:
        return 'Name are required.'
    except DictAreEmpty:
        return 'Contact with this name not found.'
    except ContactIsNotExists:
        return 'Contact with this name not found.'


def get_all_contacts(contacts):
    try:
        if len(contacts) == 0:
            raise DictAreEmpty

        text = ''

        for name, number in contacts.items():
            text += f'{name}: {number}\n'
        return text

    except DictAreEmpty:
        return 'No contacts here yet.'


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone_number(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
