from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from AWS App Runner by Atharva Palve!" # Personalized for the report name