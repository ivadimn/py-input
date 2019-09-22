from web_request import get_page, get_page_text
from bs4 import BeautifulSoup as BS
import re
from rectangle import Rect

r = Rect(5, 10)
print(r.sq)

s = "1 2 3 W w \w .w"
print(re.findall("\w", s))

page = get_page("https://yandex.ru")
print(re.findall("[А-Яа-я]", page.text))

soup = BS(page.text, "html.parser")
#print(soup.prettify())
#links = soup.find_all("a")
#for li in links:
#    print(li.get("href", ""))
