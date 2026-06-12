from flask import Flask
import random
import string

app = Flask(__name__)

@app.route("/")
def password():
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(10))
    return f"Generated Password: {password}"

if __name__ == "__main__":
    app.run(debug=True)