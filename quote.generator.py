from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "Success comes from consistency.",
    "Every day is a new beginning.",
    "Keep learning and growing.",
    "Dream big and work hard."
]

@app.route("/")
def home():
    return random.choice(quotes)

if __name__ == "__main__":
    app.run(debug=True)
