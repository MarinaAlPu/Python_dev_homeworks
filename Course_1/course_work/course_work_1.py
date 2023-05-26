# import random
from random import sample


morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

answers = []

# **Шаг 0.** Составьте список английских слов и фраз, которые будете расшифровывать.
words_to_decode = ["yesterday", "dream", "python", "dog", "peace"]
encoded_word = ""
word = ""
right_answered_words = 0
wrong_answered_words = 0
answers_to_ask = 5

# **Шаг 1.** Напишите функцию morse_encode(word), которая переводит слова на английском языке в последовательности точек и тирe.
# Например:
# morse_encode("yesterday") >>> -.--....-..-.-...--.--
# morse_encode("dream") >>> -...-...---
# morse_encode("python") >>> .--.-.---....----.
# morse_encode("dog") >>> -..-----.
# morse_encode("peace") >>> .--...--.-..
def morse_encode(word, encoded_word):
    """
    Переводит слова на английском языке в последовательности точек и тирe.
    """
    # for i in range(len(word)):
    #     if word[i] in morse:
    #         encoded_word = (encoded_word + morse[word[i]])
            # print(f"\Буква: {encoded_word}")
    # print(f"\nПечатаю слово {word} на морзе: {encoded_word}")
    # return encoded_word

    encoded_word = []

    for symbol in word:
        encoded_word.append(morse[symbol])
        word_to_decode = " ".join(encoded_word)
    return word_to_decode

# Шаг 2. Напишите функцию get_word() которая получает случайное слово из списка.
def get_word(word):
    """
    Получает случайное слово из списка
    """
    print(f"\nСейчас достанем случайное слово из списка words_to_decode в функции get_word(): {word}")
    
    word = sample(words_to_decode, 1)[0]
    print(f"\nСлучайное слово в функции get_word(): {word}")
    return word
    

# Шаг 3. Создайте в начале программы список answers = [].
# Напишите функцию print_statistics(answers) которая на основе списка answers типа [True, False, False, True, False]
# выводит статистику типа:
# Всего задачек: 5
# Отвечено верно: 2
# Отвечено неверно: 3

def print_statistics(answers, right_answered_words, wrong_answered_words):
    """
    На основе списка answers типа выводит статистику
    """

    print(f"Всего решено задачек: {len(answers)}")

    right_answered_words = answers.count(True)
    print(f"Отвечено верно: {right_answered_words}")

    wrong_answered_words = answers.count(False)
    print(f"Отвечено неверно: {wrong_answered_words}")


# Шаг 4.  При старте программы выведите приветственную информацию.

user_input = input("Сегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем")


# Шаг 5. Запустите цикл задавания вопросов. В одной игре – 5 вопросов.

# В каждой итерации:
    # - получайте случайное слово с помощью ранее написанной функции
# word = get_word()

    # - кодируйте его с помощью ранее написанной функции
# morse_encode(word)

for i in range(len(words_to_decode)):

    word = get_word(word)
    print(f"\nСлучайное слово в цикле for i in range(len(words_to_decode)): {word}")

    morse_encode(word, encoded_word)
    print(f"\nСлучайное слово закодировали: {morse_encode(word, encoded_word)}")

    # - выводите для пользователя
    print(f"\nСлово {i + 1} – {morse_encode(word, encoded_word)}")

    # - получайте ввод
    user_answer = input()

    # - сравнивайте с загаданным словом
    if user_answer != word:
        # - комментируйте верный или неверный ответ
        print(f"Неверно, {word}!")
        # - верность ответа складывайте в переменную answers
        answers.append(False)
        print(f"\nСписок верно / неверно: {answers}\n")

        answers_to_ask -= 1

    else:
        # - комментируйте верный или неверный ответ
        print(f"Верно, {word}!")
                # - верность ответа складывайте в переменную answers
        answers.append(True)

        answers_to_ask -= 1

# Слова могут повторяться во время тренировки, это не страшно.

# Шаг 6. Выведите статистику с помощью вызова ранее написанной функции

print_statistics(answers, right_answered_words, wrong_answered_words)

# Протестируйте работу приложения и отправьте ссылку на colab
