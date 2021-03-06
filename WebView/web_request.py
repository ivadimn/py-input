from requests import get


def get_link(topic):
    return "https://ru.wikipedia.org/wiki/{}".format(topic)


def get_topic_page(topic):
    html = get(get_link(topic))
    return html.text


def get_page_text(link):
    html = get(link)
    return html.text


def get_page(link):
    return get(link)