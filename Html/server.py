from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Привет! Ты добрался!!"


if __name__ == "__main__":
    app.run()