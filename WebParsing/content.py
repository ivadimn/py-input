from web_requests import get_topic_page
import re
from bs4 import BeautifulSoup as BS


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']{3,}", html_content)
    return words


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


def get_common_words1(topic):
    words_list = get_topic_words(topic)
    rate = {}
    words_set = set(words_list)
    for word in words_set:
        rate[word] = words_list.count(word)
    rate_list = list(rate.items())
    rate_list.sort(key = lambda x: -x[1])
    return rate_list


def get_topic_links(topic):
    html_content = get_topic_page(topic)
    soup = BS(html_content, "html.parser")
    links = soup.find_all("a")
    hrefs = [n.get("href", "") for n in links]
    return hrefs

def visualize_common_words(topic, down, upper):
    word_list = get_common_words(topic)
    for w in word_list[down:upper]:
        print(w)


def main():
    topic = input("Topic : ")
    hrefs = get_topic_links(topic)
    for h in hrefs:
        print(h)
    #visualize_common_words(topic, 1, 10)

main()
