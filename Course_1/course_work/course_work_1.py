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


words_to_decode = ["yesterday", "dream", "python", "dog", "peace"]
answers = []
answers_to_ask = 5


def morse_encode(word):
    """
    Переводит слова на английском языке в последовательности точек и тирe.
    """
    encoded_word = []
    for symbol in word:
        encoded_word.append(morse[symbol])
    word_to_decode = " ".join(encoded_word)
    return word_to_decode


def get_word():
    """
    Получает случайное слово из списка
    """
    word = sample(words_to_decode, 1)[0]
    return word
    

def print_statistics(answers):
    """
    На основе списка answers типа выводит статистику
    """
    print(f"Всего решено задачек: {len(answers)}")

    right_answered_words = answers.count(True)
    print(f"Отвечено верно: {right_answered_words}")

    wrong_answered_words = answers.count(False)
    print(f"Отвечено неверно: {wrong_answered_words}")


user_input = input("Сегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем")


for i in range(len(words_to_decode)):
    word = get_word()
    morse_encode(word)
    
    print(f"\nСлово {i + 1} – {morse_encode(word)}")

    user_answer = input()

    if user_answer != word:
        print(f"Неверно, {word}!")
        answers.append(False)
        answers_to_ask -= 1
    else:
        print(f"Верно, {word}!")
        answers.append(True)
        answers_to_ask -= 1


print_statistics(answers)
