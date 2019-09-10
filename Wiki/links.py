from wiki_requests import get_topic_page

from bs4 import BeautifulSoup as BS


# Получить список ссылок
def get_topic_links(topic):
    html_content = get_topic_page(topic)
    soup = BS(html_content, "html.parser")
    links = soup.find_all("a")
    hrs = [n.get("href", "") for n in links]
    return hrs


# получить соседние ссылки
def get_neighbo_links(topic):
    hrs = get_topic_links(topic)
    nlinks = [n for n in hrs if n.find("/wiki") == 0]
    # распечатем список ссылок для наглядности
    for nl in nlinks:
        print(nl)
    return nlinks


# 2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
# 3. Сложить все в один список.
def get_neighbo_pages(topic):
    nlinks = get_neighbo_links(topic)
    html_pages = [get_topic_page(n) for n in nlinks]
    return html_pages


def main():
    topic = input("Topic : ")
    pages = get_neighbo_pages(topic)
    print("Получилось всего - ", len(pages), "соседних ссылок")
    #распечатаем некоторые страницы
    for p in pages[5:7]:
        print("-----------------------------------------------------------------------------------------------")
        print(p)



main()