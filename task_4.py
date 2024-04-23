def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError as error:
            return(f"Contact with the name was not found: {error}")
        except ValueError as error:
            return(f"Give me name and phone please: {error}")
        except IndexError as error:
            return(f"Please enter the name and phone number: {error}")
    return inner

@input_error
def parse_input(user_input): # Функція для підготовки введеного корисувачем тексту. Розділяє команду та аргументи 
   cmd, *args = user_input.split()
   cmd = cmd.strip().lower()
   return cmd, *args

@input_error
def add_contact(args, contacts): # Функція для додавання контактів в словник 
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts): # Функція для зміни номеру в існуючому контакті контакті 
        name, phone = args
        if name not in contacts:
            raise KeyError(f"Contact with the name {name} was not found.")
        contacts[name] = phone
        return "Contact updated."

@input_error
def show_phone(args, contacts): # Функція для виведення номеру по імені контакта 
    *_, name = args
    value = contacts[name]
    return value

input_error
def main(): # Основна функція для обробки запитів користувача. В ній використовуються інші функції
    contacts = {}
    print("Welcome to asistant bot")

    while True: #вічний цикл 
        user_input = input("Enter a command: ")
        
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]: #команда для завершення роботи бота 
            print("Good bye")
            break
        elif command == "hello": 
            print("How can I help you?")
        elif command == "add": #команда для додавання контакту 
            print(add_contact(args, contacts))      
        elif command == "phone": # команда для виведення номеру телефону по імені
            print(show_phone(args, contacts))
        elif command == "change": #команда для змінни номера телефону по імені 
            print(change_contact(args, contacts))
        elif command == "all": #команда для виведення всіх контактів
            print(contacts)
        else:
            print("invalid command")
       
        
if __name__ == "__main__":
    main()
         
    
