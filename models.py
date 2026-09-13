from app import db

class Club(db.Model):
    code = db.Column(db.String, primary_key= True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    tags = db.relationship("Tags")

class Tags(db.Model):
    tag_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    
class ClubTags(db.Model):
    club_code = db.Column(db.String, db.ForeignKey("club.code"), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.tag_id"), primary_key = True)
    
class User(db.Model):
    username = db.Column(db.String, primary_key = True)
    
user = User(username = "josh")
db.session.add(user)
db.session.commit()



# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
