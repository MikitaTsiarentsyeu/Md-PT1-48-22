import bl

def ask(message):
    return input(f"{message}:\n")

def show_all():
    print(bl.get_all())

def add_contact():
    name = ask("Enter a new name")
    phones = ask("Enter a list of phones separated by ,")
    print(bl.add_contact(name, *phones.split(',')))

def remove_contact():
    name = ask("Enter a name")
    print(bl.remove_contact(name))

def add_number(): pass

def remove_number(): pass

def main_flow():
    while True:
        operation = input("""Enter the number of operation:
        0. Exit
        1. Show all contacts
        2. Add contact
        3. Remove contact
        4. Add phone
        5. Remove phone
        """)
        if operation == '0':
            break
        elif operation == '1':
            show_all()
        elif operation == '2':
            add_contact()
        elif operation == '3':
            remove_contact()
        elif operation == '4':
            add_number()
        elif operation == '5':
            remove_number()