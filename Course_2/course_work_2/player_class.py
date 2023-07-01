class Player:
    def __init__(self, user_name, used_words=None):
        self.user_name = user_name
        self.used_words = used_words if used_words else []

    def count_used_words(self) -> int:
        """
        Получить количество использованных слов
        """
        return len(self.used_words)

    def add_new_word(self, user_word):
        """
        Добавить слово в использованные слова
        """
        self.used_words.append(user_word)
        return self.used_words

    def is_new_word_used(self, user_word) -> bool:
        """
        Проверить использование данного слова до этого
        """
        if user_word in self.used_words:
            return True
        return False

    def __repr__(self) -> str:
        return f"Игрок '{self.user_name}'\nИспользованные слова: {self.used_words}"
