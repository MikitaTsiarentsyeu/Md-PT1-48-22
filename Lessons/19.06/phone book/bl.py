import data

def get_all():
    contacts = data.get_all_contacts()
    return '\n'.join([f"{c[0]}: {','.join(c[1])}" for c in contacts])

def format_res(res, message):
    if res:
        return f"{message}\n{get_all()}"
    else:
        return "Something went wrong"

def add_contact(name, *phones):
    res = data.add_contact(name, *phones)
    return format_res(res, "The contact was created")

def remove_contact(name):
    res = data.remove_contact(name)
    return format_res(res, "The contact was removed")