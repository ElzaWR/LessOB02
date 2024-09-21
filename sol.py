class User:
    def __init__(self, user_id, name):
        # Конструктор для класса User
        # Инкапсулируем уникальный идентификатор пользователя и имя
        self._user_id = user_id
        self._name = name
        # Уровень доступа по умолчанию — 'user' для обычных сотрудников
        self._access_level = 'user'

    # Методы для получения данных (геттеры)
    def get_user_id(self):
        # Возвращает уникальный идентификатор пользователя
        return self._user_id

    def get_name(self):
        # Возвращает имя пользователя
        return self._name

    def get_access_level(self):
        # Возвращает уровень доступа пользователя
        return self._access_level

    # Метод для изменения имени пользователя (сеттер)
    def set_name(self, name):
        # Позволяет изменить имя пользователя
        self._name = name


# Класс Admin наследует класс User
class Admin(User):
    def __init__(self, user_id, name):
        # Вызываем конструктор класса User для инициализации общих данных
        super().__init__(user_id, name)
        # Устанавливаем уровень доступа на 'admin' для администраторов
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        # Метод для добавления нового пользователя в список пользователей
        user_list.append(user)
        # Информация о добавленном пользователе
        print(f"User {user.get_name()} added by Admin {self.get_name()}")

    def remove_user(self, user_list, user_id):
        # Метод для удаления пользователя по ID из списка пользователей
        for user in user_list:
            if user.get_user_id() == user_id:
                # Если пользователь найден, удаляем его из списка
                user_list.remove(user)
                print(f"User {user.get_name()} removed by Admin {self.get_name()}")
                return
        # Если пользователь не найден, выводим сообщение
        print(f"User with ID {user_id} not found.")


# Пример использования системы
if __name__ == "__main__":
    # Создаем двух обычных пользователей
    user1 = User(1, "John Doe")
    user2 = User(2, "Jane Smith")

    print("# Создаем двух обычных пользователей")
    print(f'user1 = {user1.get_name()}')
    print(f'user2 = {user2.get_name()}')

    # Создаем администратора
    admin = Admin(0, "Admin-User")

    print("# Создаем администратора")
    print(f'Admin = {admin.get_name()}') \

    # Тестируем добавление в Систему из под абминистратора
    # Пустой список пользователей
    user_list = []

    # Администратор добавляет пользователей в систему
    print("# Администратор добавляет пользователей в систему")
    admin.add_user(user_list, user1)
    admin.add_user(user_list, user2)

    # Вывод всех пользователей в системе
    print("# Вывод всех пользователей в системе")
    for user in user_list:
        print(f"User: {user.get_name()}, Access Level: {user.get_access_level()}")

