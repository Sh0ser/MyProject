def print_menu():
    print("\nМеню:")
    print("1. Додати завдання")
    print("2. Переглянути список")
    print("3. Видалити завдання")
    print("4. Вийти")

def add_task(todo_list):
    task = input("Введіть нове завдання: ")
    todo_list.append(task)
    print("Завдання додано!")

def view_tasks(todo_list):
    if not todo_list:
        print("Список порожній.")
    else:
        print("\nСписок завдань:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def delete_task(todo_list):
    view_tasks(todo_list)
    if todo_list:
        try:
            index = int(input("Введіть номер завдання для видалення: ")) - 1
            if 0 <= index < len(todo_list):
                removed = todo_list.pop(index)
                print(f"Завдання '{removed}' видалено.")
            else:
                print("Невірний номер.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def main():
    todo_list = []
    while True:
        print_menu()
        choice = input("Оберіть опцію: ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            delete_task(todo_list)
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
