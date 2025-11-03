from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    request_url = "https://mytestapipython39.azurewebsites.net/api/"
    response = requests.get(request_url + 'getnotesmartin')
    posts = response.json()
    return render_template("index.html", posts=posts)


def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
