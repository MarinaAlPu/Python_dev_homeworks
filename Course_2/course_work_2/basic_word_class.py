class BasicWord:
    def __init__(self, original_word, valid_words):
        self.original_word = original_word
        self.valid_words = valid_words

    def is_word_valid(self, user_word) -> bool:
        """
        Проверяет введённое слово в списке допустимых подслов
        """
        if user_word in self.valid_words:
            return True
        else:
            return False

    def count_valid_words(self) -> int:
        """
        Подсчитывает количество подслов
        """
        return len(self.valid_words)

    def __repr__(self) -> str:
        return f"Начальное слово: {self.original_word}" \
               f"\nДопустимые подслова: {self.valid_words}"
