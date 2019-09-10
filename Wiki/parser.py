from requests import get

def get_info(text):
    link = 'https://ru.wikipedia.org/wiki/' + text.capitalize()
    return link

def get_page(text):
    link = get_info(text)
    html_content = get(link).text
    return html_content

if __name__  == '__main__':
    print(get_page('россия'))