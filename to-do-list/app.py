from http.cookiejar import debug

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"


@app.route('/about')
def index2():
    return "I am a G"


if __name__ == "__main__":
    app.run(debug=True)