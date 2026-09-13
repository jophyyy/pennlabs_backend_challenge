import os
import json

from app import app, db, DB_FILE

from models import *

def create_user():
    user = User(username = "josh")
    db.session.add(user)
    db.session.commit()

def load_data():
    with open("clubs.json", "r") as file:
        data = json.load(file)
        

# No need to modify the below code.
if __name__ == "__main__":
    # Delete any existing database before bootstrapping a new one.
    LOCAL_DB_FILE = "instance/" + DB_FILE
    if os.path.exists(LOCAL_DB_FILE):
        os.remove(LOCAL_DB_FILE)

    with app.app_context():
        db.create_all()
        create_user()
        load_data()

print(data)