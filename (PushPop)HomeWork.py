from typing import Tuple, Dict


class InputError(Exception):
    def __init__(self, text):
        self.text = text


def get_name() -> Tuple[str, str]:
    full_name = input('Enter full name:').split()
    try:
        if len(full_name) > 2:
            raise InputError('Len of full name > 2')
        first_name, last_name = full_name[0], full_name[1]
    except InputError:
        print('The full name must be 2 words. No more and no less.')
        get_name()
    except IndexError:
        print('The full name must be 2 words. No more and no less.')
        get_name()
    return first_name, last_name


def push() -> None:
    key = input('Enter Key: ')
    value = input('Enter Value: ')
    DATA_STACK[key] = value


def pop() -> None:
    key = input('Enter key: ')
    try:
        return print(DATA_STACK[key])
    except KeyError:
        print('Key not exist')


FUNC_CONTAINER = {
    "push": push,
    "pop": pop
}
DATA_STACK: Dict[str, str] = {}

if __name__ == "__main__":
    fullname = get_name()
    while True:
        choice = input('Enter your choice(push or pop): ')
        try:
            FUNC_CONTAINER[choice]()
        except KeyError:
            print("Only push or pop")
