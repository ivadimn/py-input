import re
from requests import get
from urllib.parse import unquote

# функция формирования начальной ссылки
def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link

# функция получения содержимого начальной ссылки
def get_topic_page(topic):
    link = get_link(topic)
    html_content = get(link).text
    return html_content

# функция отбора ссылок на русские статьи на начальной странице
def get_topic_page_links(topic):
    html_content = get_topic_page(topic)
    links = re.findall('(/wiki/[%A-Z0-9]+)"', html_content)
    link_list = []
    ru_link_list = []
    for l in links:
        l = 'https://ru.wikipedia.org' + unquote(l)
        link_list.append(l)
    ru_link_list = re.findall('https://ru.wikipedia.org/wiki/[а-яА-Я]+', str(link_list))
    return ru_link_list

# Функция выбора слов на всех страницах. Ограничил диапазон, очень много ссылок
def get_topic_words(topic):
    link = get_topic_page_links(topic)
    all_words = []
    for l in link[0:10]:
        html_content = get(l).text
        words = re.findall("[а-яА-Я\-\']{3,}", html_content)
        for word in words:
            all_words.append(word)
    return all_words

# функция подсчёта повторяемости слов
def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key = lambda x: -x[1])
    return rate_list

# 10 самых повторяемых слов
def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[0:10]:
        print(w[0])

# задание ключевой темы страницы
def main():
    topic = input("Topic: ")
    visualize_common_words(topic)
