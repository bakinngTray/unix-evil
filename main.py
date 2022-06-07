# This is a sample Python script.

from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('Novyi_774_Yunix.pdf')


if __name__ == "__main__":
    app.run()