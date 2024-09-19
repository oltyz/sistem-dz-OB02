# main.py

from users import create_user, create_admin

# Создаем главного администратора, который может добавлять/удалять других администраторов
main_admin = create_admin(1, "Главный Администратор")

# Функция для обработки ввода пользователя
def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Добавить администратора")
        print("4. Удалить администратора")
        print("5. Показать всех пользователей")
        print("6. Показать всех администраторов")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_user_interface(main_admin)
        elif choice == '2':
            remove_user_interface(main_admin)
        elif choice == '3':
            add_admin_interface(main_admin)
        elif choice == '4':
            remove_admin_interface(main_admin)
        elif choice == '5':
            main_admin.list_users()
        elif choice == '6':
            main_admin.list_admins()
        elif choice == '7':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Интерфейс для добавления пользователя
def add_user_interface(admin):
    user_id = int(input("Введите ID пользователя: "))
    name = input("Введите имя пользователя: ")
    user = create_user(user_id, name)
    admin.add_user(user)

# Интерфейс для удаления пользователя
def remove_user_interface(admin):
    user_id = int(input("Введите ID пользователя, которого хотите удалить: "))
    admin.remove_user(user_id)

# Интерфейс для добавления администратора
def add_admin_interface(admin):
    admin_id = int(input("Введите ID администратора: "))
    name = input("Введите имя администратора: ")
    new_admin = create_admin(admin_id, name)
    admin.add_admin(new_admin)

# Интерфейс для удаления администратора
def remove_admin_interface(admin):
    admin_id = int(input("Введите ID администратора, которого хотите удалить: "))
    admin.remove_admin(admin_id)

# Запуск программы
menu()
