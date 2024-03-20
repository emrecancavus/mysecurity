from flask import Flask, render_template, url_for, json, request
import requests
import json
import urllib.parse


class MaliciousURLScanner:
    def __init__(self, api_key):
        self.api_key = api_key

    def scan_url(self, url, strictness=0):

        url = f'https://www.ipqualityscore.com/api/json/url/{self.api_key}/{urllib.parse.quote_plus(url)}'
        params = {'strictness': strictness}
        response = requests.get(url, params=params)
        return json.loads(response.text)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def security():
    results = {}
    if request.method == "POST":
        api_key = 'JwE3UPSsGAS3fusxpXZ9FZxFrgEYuJuU'
        scanner = MaliciousURLScanner(api_key)
        input_data = request.form['input_data']
        URL = input_data
        strictness = 0
        results = scanner.scan_url(URL, strictness)
        if 'success' in results and results['success'] == True:
            return render_template("son.html", results = results)
    else:
        return render_template("son.html", results = results)
    
if __name__ == "__main__":
    app.run(debug=True)
