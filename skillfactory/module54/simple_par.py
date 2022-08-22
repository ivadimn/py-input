import requests
import lxml.html
from lxml import etree

html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('python_org.html', lxml.html.HTMLParser())

#ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')
ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li')

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тег <a># )
    t = li.find("time")
    dt = t.get("datetime")
    print(dt[:10], a.text)  # из этого тега забираем текст, это и будет нашим названием


