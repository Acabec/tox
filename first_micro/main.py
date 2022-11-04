from flask import Flaskdeta new --project <your-project>

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"