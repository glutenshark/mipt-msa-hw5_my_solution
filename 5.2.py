import requests
import re

# from line_profiler import profile
# from memory_profiler import profile

#@profile
def get_text(url):
    # Получаем ответ по HTTP GET запросу.
    response = requests.get(url)
    # Возвращаем текст ответа.
    return response.text

#@profile
def count_word_frequencies(word_to_url, word_list):
    # Проходим по списку слов из загруженного текста.
    for word in word_to_url:
        # Если слово присутствует в словаре (из файла words.txt).
        if word in word_list:
            # Увеличиваем значение счетчика этого слова на 1.
            word_list[word] = word_list[word] + 1
    # Возвращаем словарь.
    return word_list

#@profile
def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"
    
    # Открываем файл и обрабатываем его содержимое:
    # - Читаем и разбиваем на строки;
    # - Фильтруем пустые строки;
    # - Убираем лишние пробелы;
    # - Собираем уникальные слова (через множество) и создаем словарь с начальными значениями 0.
    with open(words_file, 'r', encoding='utf-8') as file:
        word_list = dict.fromkeys(
            set(map(str.strip, filter(None, file.read().splitlines()))),
            0
        )
        # Альтернативный вариант: {line.strip(): 0 for line in file if line.strip()}
    
    # Получаем текст по URL.
    response = get_text(url)
    # Удаляем знаки препинания (заменяем все символы, не являющиеся буквами, цифрами или пробелами, на пробелы).
    response = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', " ", response)
    # Приводим текст к нижнему регистру и разбиваем на слова по пробельным символам.
    word_to_url = list(response.lower().split())
    
    # Получаем словарь вхождений слов из файла в текст.
    frequencies = count_word_frequencies(word_to_url, word_list)
    # Выводим словарь и количество уникальных слов.
    print(frequencies, len(frequencies))

if __name__ == "__main__":
    main()
