def parse_input(user_input):
  """
  Функція розбирає введені користувачем слова.

  Args:
    user_input: Рядок введення користувача.

  Returns:
    Кортеж з командою та аргументами.
  """
  cmd, *args = user_input.split()
  cmd = cmd.strip().lower()
  return cmd, args

def add_contact(args, contacts):
  """
  Функція додає новий контакт до словника.

  Args:
    args: Список з ім'ям та телефоном нового контакту.
    contacts: Словник для зберігання контактів.

  Returns:
    Рядок з повідомленням про успішне додавання.
  """
  name, phone = args
  contacts[name] = phone
  return "Contact added."

def change_contact(args, contacts):
  """
  Функція змінює номер телефону для існуючого контакту.

  Args:
    args: Список з ім'ям та новим номером телефону контакту.
    contacts: Словник для зберігання контактів.

  Returns:
    Рядок з повідомленням про успішну зміну.
  """
  name, phone = args
  if name not in contacts:
    return "Contact not found."
  contacts[name] = phone
  return "Contact updated."

def show_phone(args, contacts):
  """
  Функція виводить номер телефону для контакту.

  Args:
    args: Список з ім'ям контакту.
    contacts: Словник для зберігання контактів.

  Returns:
    Рядок з номером телефону або повідомлення про помилку.
  """
  name = args[0]
  if name not in contacts:
    return "Contact not found."
  return contacts[name]

def show_all(contacts):
  """
  Функція виводить всі збережені контакти.

  Args:
    contacts: Словник для зберігання контактів.

  Returns:
    None.
  """
  for name, phone in contacts.items():
    print(f"{name}: {phone}")

def main():
  """
  Головна функція бота.
  """
  contacts = {}
  print("Welcome to the assistant bot!")
  while True:
    user_input = input("Enter a command: ")
    command, args = parse_input(user_input)

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
      print(show_phone(args, contacts))
    elif command == "all":
      show_all(contacts)
    else:
      print("Invalid command.")

if __name__ == "__main__":
  main()