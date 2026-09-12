from app import db

class Club(db.Model):
    code = db.Column(db.String, primary_key= true)
    name = db.Column(db.String)
    description = db.Column(db.String)
    tags = db.relationship("Tags")

class Tags(db.Model):
    tag_id = db.Column(db.Integer, primary_key = true)
    name = db.Column(db.String)
    




# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
