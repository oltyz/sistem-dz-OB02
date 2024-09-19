# users.py

# Класс User для обычных пользователей
class User:
    def __init__(self, user_id, name, access_level='user'):
        """Инициализация атрибутов пользователя"""
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для изменения имени пользователя
    def set_name(self, new_name):
        self.__name = new_name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level

    # Строковое представление пользователя
    def __str__(self):
        return f"User ID: {self.__user_id}, Имя: {self.__name}, Уровень доступа: {self.__access_level}"


# Класс Admin, наследующий класс User
class Admin(User):
    def __init__(self, user_id, name):
        """Инициализация атрибутов администратора"""
        super().__init__(user_id, name, access_level='admin')
        self.__user_list = []  # Список пользователей
        self.__admin_list = []  # Список администраторов

    # Метод для добавления пользователя
    def add_user(self, user):
        self.__user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен в систему.")

    # Метод для удаления пользователя по ID
    def remove_user(self, user_id):
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                self.__user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален из системы.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для добавления администратора
    def add_admin(self, admin):
        self.__admin_list.append(admin)
        print(f"Администратор {admin.get_name()} добавлен в систему.")

    # Метод для удаления администратора по ID
    def remove_admin(self, admin_id):
        for admin in self.__admin_list:
            if admin.get_user_id() == admin_id:
                self.__admin_list.remove(admin)
                print(f"Администратор {admin.get_name()} удален из системы.")
                return
        print(f"Администратор с ID {admin_id} не найден.")

    # Метод для вывода списка пользователей
    def list_users(self):
        if self.__user_list:
            print("Список пользователей:")
            for user in self.__user_list:
                print(user)
        else:
            print("Нет зарегистрированных пользователей.")

    # Метод для вывода списка администраторов
    def list_admins(self):
        if self.__admin_list:
            print("Список администраторов:")
            for admin in self.__admin_list:
                print(admin)
        else:
            print("Нет зарегистрированных администраторов.")


# Функции для создания пользователей и администраторов

def create_user(user_id, name):
    """Функция для создания обычного пользователя"""
    return User(user_id, name)


def create_admin(user_id, name):
    """Функция для создания администратора"""
    return Admin(user_id, name)

