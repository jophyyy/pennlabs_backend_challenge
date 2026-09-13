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

@app.route("/api/user/<username>")
def get_user_profile(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "username": user.username,
        "name": user.name
    })
    
@app.route("/api/clubs", methods=["POST"])
def create_club():
    data = request.get_json()
    
    if not data or "code" not in data or "name" not in data:
        return jsonify({"message": "Code and name are required"}), 400
    if Club.query.filter_by(code=data["code"]).first():
        return jsonify({"message": "Club with this code already exists"}), 400
    
    new_club = Club(
        code=data["code"],
        name=data["name"],
        description=data.get("description", "")
    )
    db.session.add(new_club)
    
    for tag_name in data.get("tags", []):
        tag = Tags.query.filter_by(name=tag_name).first()
        if not tag:
            tag = Tags(name=tag_name)
            db.session.add(tag)
            db.session.flush()
        relationship = ClubTags(club_code=new_club.code, tag_id=tag.tag_id)
        db.session.add(relationship)
        
    db.session.commit()
    
    return jsonify({"message": "Club created successfully"}), 201

if __name__ == "__main__":
    app.run()
    
