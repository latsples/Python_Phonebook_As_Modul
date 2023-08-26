import text

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)

def print_message(msg: str):                # Эта функция обрамляет сообщение сверху и снизу знаками "=" 
    print('\n' + '=' * len(msg))            # (можно заменить на любой)другой. Короче - для красоты. Стоит запомнить!!!
    print(msg)
    print('=' * len(msg) + '\n')



def show_book(book: dict[int, list[str]], msg: str):
    if book:
        print('\n' + '*' * 67)
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[3]:<20}') # Выравнивание строки (три знака, выравнивание
        print('*' * 67 + '\n')                                                   # по правому краю) и (три раза по 20 знаков
    else:                                                                        # с выравниванием по левому краю). Красивость
        print_message(msg)


def input_contact(msg: str) -> list[str]:
    contact = []
    for input_text in msg:
        contact.append(input(input_text))
    return contact


def input_request(msg: str) -> str:
    return input(msg)
