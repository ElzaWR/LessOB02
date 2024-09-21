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
