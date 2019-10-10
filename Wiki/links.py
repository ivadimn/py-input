from wiki_requests import get_topic_page

from bs4 import BeautifulSoup as BS

mos_metro = "Список_станций_Московского_метрополитена"

# Получить список ссылок
def get_topic_links(topic):
    html_content = get_topic_page(topic)
    soup = BS(html_content, "html.parser")
    links = soup.find_all("tr")
    print(links)
    #hrs = [n.get("", "") for n in links]
    #//return hrs

def get_topic_tables(topic):
    html_content = get_topic_page(topic)
    soup = BS(html_content, "html.parser")
    tables = soup.find_all("table")
    tbs = soup.select("table.standard");
    for t in tbs:
        trs = t.select("tr")
        print(len(trs))
    hrs = [t.get("class", "") for t in tables]
    print(hrs)
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
<<<<<<< Updated upstream
    tables = get_topic_tables(mos_metro)
=======
    get_topic_links("")


>>>>>>> Stashed changes

main()