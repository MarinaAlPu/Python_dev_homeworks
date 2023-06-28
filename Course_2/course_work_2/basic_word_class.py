"""
Создайте класс `BasicWord` в отдельном файле. Этот класс будет содержать в себе:
**Поля:**
- исходное слово,
- набор допустимых подслов.

Не забудьте определить метод  `__repr__`

При инициализации экземпляру задаются: исходное слово и набор допустимых слов, составленных из исходного.
"""


class BasicWord:
    def __init__(self, original_word, valid_words):
        self.original_word = original_word
        self.valid_words = valid_words

    def is_word_valid(self) -> bool:
        """
        Проверяет введённое слово в списке допустимых подслов
        """
        pass

    def count_valid_words(self) -> int:
        """
        Подсчитывает количество подслов
        """
        pass

    def __repr__(self) -> str:
        return f"Начальное слово: {self.original_word}" \
               f"\nДопустимые подслова: {self.valid_words}"


# basic_word = BasicWord(original_word, valid_words)
# print(basic_word)
