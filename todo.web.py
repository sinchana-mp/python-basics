from flask import Flask

app = Flask(__name__)

tasks = ["Learn Python", "Learn Flask", "Build Projects"]

@app.route("/")
def home():
    result = "<h1>My To-Do List</h1>"

    for task in tasks:
        result += f"<p>• {task}</p>"

    return result

if __name__ == "__main__":
    app.run(debug=True)