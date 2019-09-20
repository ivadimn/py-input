from web_requests import get_topic_page, get_page
from bs4 import BeautifulSoup as BS

link = "https://yandex.ru"
html = get_page(link)
soup = BS(html, "html.parser")
print(soup.get_text())
print(soup.get("div"))
links = soup.find_all("a")
hrs = [n.get("class", "") for n in links]
for h in hrs:
    print(h)

#for l in links:
#    print(l.attrs)

