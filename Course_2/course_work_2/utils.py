import requests
from random import choice

from basic_word_class import BasicWord


def load_random_word() -> BasicWord:
    """
    Получает список слов с внешнего ресурса, выберает случайное слово,
    создаёт экземпляр класса BasicWord, возвращает этот экземпляр.
    """
    PATH = "https://www.jsonkeeper.com/b/2FMD"

    resp = requests.get(PATH)
    data = resp.json()
    one_word_info = choice(data)
    basic_word = BasicWord(one_word_info["word"], one_word_info["subwords"])
    return basic_word
