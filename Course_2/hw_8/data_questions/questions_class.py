class Question:
    def __init__(self, question_text, question_level, right_answer):
        self.question_text = question_text
        self.question_level = question_level
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.points = int(self.question_level) * 10

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов."""
        return self.points

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает с верным ответов иначе False."""
        return self.user_answer == self.right_answer

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5"""
        return f"Вопрос: {self.question_text}\nСложность: {self.question_level}/5"

    def build_feedback(self) -> str:
        """Возвращает:
        1. Ответ верный, получено __ баллов
        2. Ответ неверный, верный ответ ___"""
        if self.is_correct(): # == True:
            return f"Ответ верный, получено {self.points} баллов"
        return f"Ответ неверный, верный ответ - {self.right_answer}"

    def __repr__(self):
        return f"\nЯ экземпляр с параметрами:\nвопрос - {self.question_text}\nсложность - {self.question_level}\nверный ответ - {self.right_answer}" \
               f"\nза меня дают - {self.points} баллов"
