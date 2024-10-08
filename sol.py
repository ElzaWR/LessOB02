class User:
    def __init__(self, user_id, name):
        # Конструктор для класса User
        # Инкапсулируем уникальный идентификатор пользователя и имя
        self.__user_id = user_id
        self.__name = name
        # Уровень доступа по умолчанию — 'user' для обычных сотрудников
        self.__access_level = 'user'

    # Методы для получения данных (геттеры)
    def get_user_id(self):
        # Возвращает уникальный идентификатор пользователя
        return self.__user_id

    def get_name(self):
        # Возвращает имя пользователя
        return self.__name

    def get_access_level(self):
        # Возвращает уровень доступа пользователя
        return self.__access_level

    # Метод для изменения имени пользователя (сеттер)
    def set_name(self, name):
        # Позволяет изменить имя пользователя
        self.__name = name


# Класс Admin наследует класс User
class Admin(User):
    def __init__(self, user_id, name):
        # Вызываем конструктор класса User для инициализации общих данных
        super().__init__(user_id, name)
        # Устанавливаем уровень доступа на 'admin' для администраторов
        self.__access_level = 'admin'

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
 \
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

    # Тестируем удаление из Системы из под администратора
    # Администратор удаляет пользователя с ID 1
    print("# Администратор удаляет пользователя с ID 1")
    admin.remove_user(user_list, 1)

    # Вывод оставшихся пользователей после удаления
    print("# Вывод оставшихся пользователей после удаления")
    for user in user_list:
        print(f"User: {user.get_name()}, Access Level: {user.get_access_level()}")

    # Тестируем инкапсуляцию
    print("# Тестируем инкапсуляцию")
    # Пытаемся напрямую получить доступ к защищенному атрибуту (неправильно)
    print("# Пытаемся напрямую получить доступ к защищенному атрибуту (неправильно)")
    try:
        print(user1.__name)  # Доступ к защищенному атрибуту, должен быть скрыт
    except AttributeError as e:
        print(e)

    # Правильный доступ через геттер
    print("# Правильный доступ через геттер")
    print("User name:", user1.get_name())  # Корректный доступ через метод

    # Попытка изменения защищенного атрибута напрямую (неправильно)
    print("# Попытка изменения защищенного атрибута напрямую (неправильно)")
    try:
        print(f'Было user1 = {user1.get_name()}')
        print(f'Попробуем изменить на John Smith')
        user1.__name = "John Smith"  # Не сработает из-за инкапсуляции
        print(f'Теперь user1 = {user1.get_name()}')
    except AttributeError as e:
        print("Error:", e)

    # Изменение имени через сеттер
    print("# Правильный доступ через сеттер")
    user1.set_name("John Smith")
    print("Updated User name:", user1.get_name())  # Корректное изменение через метод
    print(f'Теперь user1 = {user1.get_name()}')
