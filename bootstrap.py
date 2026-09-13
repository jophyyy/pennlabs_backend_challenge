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
        for club in data:
            club_obj = Club(
                code = club["code"],
                name = club["name"],
                description = club["description"]
            )
        db.session.add(club_obj)
        for tag in club["tags"]:
            existing_tag = Tags.query.filter_by(name=tag).first()
            if existing_tag is None:
                existing_tag = Tags(name=tag)
                db.session.add(existing_tag)
                
            print(existing_tag.name)

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