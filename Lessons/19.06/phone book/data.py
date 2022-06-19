repo = {1: ("test name", ["2456789"])}

def get_all_contacts():
    return repo.values()

def add_contact(name, *phones):
    try:
        new_contact = (name, phones)
        for i in range(1, len(repo)+2):
            if i not in repo:
                repo[i] = new_contact
                break
        return True
    except:
        return False

def remove_contact(name):
    for k, v in repo.items():
        if v[0] == name:
            del repo[k]
            return True
    return False

def add_number(name, phone): pass

def remove_number(name, phone): pass