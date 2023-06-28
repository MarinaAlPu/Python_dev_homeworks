"""
Создайте класс `Player`. Этот класс будет содержать в себе:

**Поля:**
- имя пользователя,
- использованные слова пользователя.

Не забудьте определить метод  `__repr__`
"""


class Player:
    def __init__(self, user_name, used_words):
        self.user_name = user_name
        self.used_words = used_words

    def count_used_words(self) -> int:
        """
        Получить количество использованных слов
        """
        pass

    def add_new_word(self):
        """
        Добавить слово в использованные слова
        """
        pass

    def is_new_word_used(self) -> bool:
        """
        Проверить использование данного слова до этого
        """
        pass

    def __repr__(self) -> str:
        return f"Игрок {self.user_name}\nИспользованные слова: {self.used_words}"


player = Player("Марина", "разные другие слова")
print(player)
