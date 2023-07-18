contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Я не знайшов контакт"
        except ValueError:
            return "Неправильний формат вводу"
        except IndexError:
            return "Ти вказав неправильний формат команди. Будь ласка, спробуй ще раз або введи info для допомоги"
    return wrapper


@input_error
def hello_command(*args):
    return "Чим можу допомогти?"


@input_error
def info_command(*args):
    info_text = '''Доступні команди:
hello -- я привітаюсь.
info -- інформація про доступні команди.
add Ім'я номер_телефону -- додам до списку контакт з номером телефону.
change Ім'я номер_телефону -- зміню номер телефону для контакту.
phone Ім'я -- покажу номер телефону контакту.
show all -- покажу всі збережені контакти з номерами телефонів.
good bye або close або exit -- закінчу роботу
    '''
    return info_text


@input_error
def add_contact_command(*args):
    name = args[0]
    phone = args[1]
    if name in contacts and contacts[name] == phone:
        return "У цього контакту вже записаний цей номер телефону. Якщо хочеш його замінити, обери команду change"
    else:
        contacts[name] = phone
        return f'Я додав контакт "{name}" з номером "{phone}" у список контактів'


@input_error
def contact_change_command(*args):
    name = args[0]
    phone = args[1]
    if name in contacts:
        old_phone = contacts[name]
        contacts[name] = phone
        return f"Я замінив номер телефону для контакту {name}: номер {old_phone} замінений на {phone}"
    else:
        raise KeyError

@input_error
def phone_command(*args):
    name = args[0]
    if name in contacts:
        return f"Номер телефону для контакту {name}: {contacts[name]}"
    else:
        raise KeyError

@input_error
def show_all_contacts_command():
    if contacts:
        result = "Це твій список контактів:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "Твій список контактів порожній"


@input_error
def bad_command(*args):
    return "Я не впізнав команду. Будь ласка, спробуй ще раз або введи info для допомоги"


@input_error
def exit_command(*args):
    return "Good bye!"


@input_error
def input_parser(user_input):
    for command, arguments in COMMANDS.items():
        for argument in arguments:
            if user_input.lower().startswith(argument):
                if user_input[:len(argument)] != argument:
                    user_input = argument + user_input[len(argument):]
                return command(*user_input.replace(argument, "").strip().split())
    return bad_command()


COMMANDS = {
        info_command: ["info"],
        hello_command: ["hello"],
        add_contact_command: ["add"],
        contact_change_command: ["change"],
        phone_command: ["phone"],
        show_all_contacts_command: ["show all"],
        exit_command: ["good bye", "close", "exit"]
        }
    

def main():
    print("Вітаю! Я бот-помічник.")
    while True:
        user_input = input('\nВведи команду ("info" для допомоги) >>> ')
        result = input_parser(user_input)
        print(result)
        if result == "Good bye!":
            break
    
if __name__ == "__main__":
    main()