from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FREEBOX_IP = "192.168.0.2"
REMOTE_CODE = "55984265"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    key = request.form["key"]
    url = f"http://{FREEBOX_IP}/pub/remote_control?code={REMOTE_CODE}&key={key}"
    r = requests.get(url)
    return ("", 204)  # Pas de contenu, juste retour rapide

if __name__ == "__main__":
    app.run(debug=True)
