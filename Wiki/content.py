from requests import get


def get_topic_link(topic):
    return "https://ru.wikipedia.org/wiki/{}".format(topic)


def get_topic_text(topic):
    html = get(get_topic_link(topic))
    return html.text


def get_topic_words(topic, len_word):
    text = get_topic_text(topic)
    reg_exp = "\\b\w{" + str(len_word) + ",}\\b"
    print(reg_exp)


get_topic_words("Россия", 3)