from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! Proiectul tău a pornit cu succes."

if __name__ == "__main__":
    app.run(debug=True)
