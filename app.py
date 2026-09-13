from flask import Flask, request, jsonify
from models import *

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db.init_app(app)




@app.route("/")
def main():
    return "Welcome to Penn Club Review!"


@app.route("/api")
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})


@app.route("/api/clubs")
def clubs():
    clubs = Club.query.all()
    print(clubs)
    return "check terminal"
    


if __name__ == "__main__":
    app.run()
