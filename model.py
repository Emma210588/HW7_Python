phone_book = []
path = 'phone_book.txt'


def get_phone_book():
    global phone_book
    return phone_book


def update_phone_book(contact: list): 
    global phone_book
    phone_book.append(contact)


def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))


def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def search_contact(search: str):
    global phone_book
    search_result = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_result.append(line)
                break
    return search_result


def delete_contact(name: str):
    global phone_book
    for line in phone_book:
        if name == line[0]:
            phone_book.remove(line)
            break
    

def change_contact(name, select, n_value):
    global phone_book
    for line in phone_book:
        if name == line[0]:
            if select == 1:
                line[0] = n_value
            elif select == 2:
                line[1] = n_value
            elif select == 3:
                line[2] = n_value
            break
        
            
