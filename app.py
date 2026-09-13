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
    search_term = request.args.get("search")
    if search_term:
        clubs = Club.query.filter(Club.name.ilike(f"%{search_term}%")).all()
    else:
        clubs = Club.query.all()
    
    
    clubs_data = []
    
    for club in clubs:
        club_tag_entries = ClubTags.query.filter_by(club_code=club.code).all()
        tag_names=[]
        for entry in club_tag_entries:
            tag = Tags.query.filter_by(tag_id=entry.tag_id).first()
            if tag:
                tag_names.append(tag.name)
                
        clubs_data.append({
            "code": club.code,
            "name": club.name,
            "description": club.description,
            "tags": tag_names
        })
    
    return jsonify(clubs_data)

@app.route("/api/tags")
def tags():
    tags = Tags.query.all()
    tag_data = []
    
    for tag in tags:
        count = ClubTags.query.filter_by(tag_id=tag.tag_id).count()
        tag_data.append({
            "tag": tag.name,
            "count": count
        })
        
    return jsonify(tag_data)

if __name__ == "__main__":
    app.run()
