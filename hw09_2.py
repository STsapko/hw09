contacts = {}

def help(*args):
    return \
"""menu:
    hello
    add
    change
    phone
    show all
    exit (close, good bye)
    """

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "No such name"
        except ValueError:
            return "Enter user name"
    return wrapper

def say_hello(*args):
    return 'How can I help you?'

def exit(*args):
    return 'Good bye!'

def no_command(*args):
    return "Unknown operation, try again."

@input_error
def add_contact(*args):
    list_of_params = args[0].split()
    name = list_of_params[0]
    phone = list_of_params[1]
    contacts[name] = phone
    return f'added contact Name: {name}, Phone: {contacts[name]}'

@input_error
def change_contact(*args):
    list_of_params = args[0].split()
    name = list_of_params[0]
    phone = list_of_params[1]
    old_phone = contacts[name]
    contacts[name] = phone
    return f'changed contact Name: {name}, Phone: {contacts[name]} (Phone before: {old_phone})'

@input_error
def show_phone(*args):
    list_of_params = args[0].split()
    name = list_of_params[0]
    return f'contact Name: {name}, Phone: {contacts[name]}'

def show_all_contacts(*args):
    result = ''
    for name, phone in contacts.items():
        result += f'Name {name}: Phone: {phone}'+'\n'
    if not result:
        return 'No contacts yet'
    return result

OPERATIONS = {
    add_contact: 'add',
    change_contact: 'change',
    show_phone: 'phone',
    show_all_contacts: 'show all',
    say_hello: 'hello',
    exit: ['exit', 'close','goodbay'],
}

def get_operation(text: str):
    for operation, kword in OPERATIONS.items():
        # if [el for el in list(kword) if text.startswith(el)]:
        if type(kword) == str:
            if text.lower().startswith(kword):
                return operation, text[len(kword):].strip()
        if type(kword) == list:
            for k in kword:
                if text.startswith(k):
                    return operation, text[len(kword):].strip()
    return no_command, None
     
def main():
    print(help())
    while True:
        user_input = input('>>> ')
        operation, data = get_operation(user_input)
        print(operation(data))
        if operation == exit:
            break

if __name__ == '__main__':
    main()