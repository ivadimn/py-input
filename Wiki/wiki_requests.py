from requests import get


def get_link(topic):
    return "https://ru.wikipedia.org/wiki/Список_станций_Московского_метрополитена"


def get_topic_page(topic):
    html = get(get_link(topic))
    return html.text

