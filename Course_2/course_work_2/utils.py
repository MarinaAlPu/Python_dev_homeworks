import requests
from random import shuffle

from basic_word_class import BasicWord


def load_random_word() -> BasicWord:
    """
    Получает список слов с внешнего ресурса, выберает случайное слово,
    создаёт экземпляр класса BasicWord, возвращает этот экземпляр.
    """
    # Получить список слов с внешнего ресурса
    PATH = "https://www.jsonkeeper.com/b/2FMD"
    basic_words_list = []
    # words_from_random_word_list = []

    resp = requests.get(PATH)
    data = resp.json()
    print(data)
    # print(type(data))

    # Получить список исходных слов
    for d in data:
        # question = Question(q["q"], q["d"], q["a"])
        basic_word = BasicWord(d["word"], d["subwords"])
        # print(basic_word)

        basic_words_list.append(basic_word)
        # print(basic_words_list)

        shuffle(basic_words_list)
        # print(basic_words_list)

        # words_list.append(d["word"])
        # words_from_random_word_list.append(d["subwords"])
    # print(words_list)
    # print(type(words))
    # print(words_from_random_word_list)

    # # Выбрать случайное слово
    # shuffle(words_list)
    # print(f"перемешанный список {words_list}")
    #
    # random_word = words_list[0]
    # print(f"случайное слово {random_word}")
    #
    # # Получить набор допустимых слов, составленных из исходного слова
    # for
    #
    # print(f"набор слов {words_from_random_word_list} из случайного слова {random_word}")

    # words_from_random_word =



    # Создать экземпляр класса BasicWord
    # basic_word = BasicWord(random_word, words_from_random_word)
    print(basic_words_list[0])
    # return basic_words_list[0]


load_random_word()