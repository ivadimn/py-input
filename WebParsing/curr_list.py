from collections import namedtuple
from dataclasses import dataclass
import requests
import json
from bs4 import BeautifulSoup as BS


@dataclass
class Currency:
    code: str
    name: str

    def __eq__(self, other):
        return self.code == other.code

    def __str__(self):
        return "{0}: {1}".format(self.code, self.name)


url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D1%85_%D0%B2%D0%B0%D0%BB%D1%8E%D1%82"
response = requests.get(url)
soup = BS(response.text, "html.parser")

table = soup.find("tbody")
rows = table.find_all("tr")
currs = []
for row in rows:
    curr = []
    cols = row.find_all("td")
    for i, col in enumerate(cols):
        if i == 1:
            raw_name: str = col.text[:-1]
            if "(" in raw_name:
                si = raw_name.index("(")
                name = raw_name[:si]
                full_name = raw_name[si + 1:-1]
            else:
                name = raw_name
                full_name = ""
            curr.append(name.lower())
            curr.append(full_name)
        elif i == 6:
            curr.append(col.text[:-1])
    if len(curr) == 3:
        currs.append(curr)

curr_dict = dict()
for i, curr in enumerate(currs):
    name = curr[0]
    if name in curr_dict:
        lst = curr_dict.get(name)
        for item in lst:
            if item[0] == curr[2]:
                break
        else:
            lst.append((curr[2], curr[1]))
    else:
        curr_dict[name] = [(curr[2], curr[1])]

for key, val in curr_dict.items():
    print(key, val)

with open("curr_list.json", "w") as f:
    json.dump(curr_dict, f)
