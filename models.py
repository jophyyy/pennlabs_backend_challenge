from app import db

class Club(db.Model):
    code = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    tags_id = db.Column(db.String)






# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
