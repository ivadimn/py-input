def index() -> str:
    with open("templates/index.html", "r") as template:
        return template.read()

def blog() -> str:
    with open("templates/blog.html", "r") as template:
        return template.read()

