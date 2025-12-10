from flask import Blueprint, render_template, request
from repositories.club_repository import ClubRepository
from models.club import Club
from models.office import Office

browse_bp = Blueprint("browse", __name__)
repo = ClubRepository()

# dummy data for runtime memory
clubs = [
    Club(
        "1", 
        "Robotics club", 
        "We build robots and compete.",
        "Academic",
        ["Ali", "Omar"], 
    ),
    Club(
        "2", 
        "Acting & Theatre", 
        "We perform plays and drama.",
        "Social",
        ["Lina", "Sara"],
    )
]

offices = [
    Office(
        "CATS", 
        "Career Advising Office, We help you find jobs.", 
        ["Dr. Maha"],
        "maha@ust.edu.eg" 
    ),
    Office(
        "Housing", 
        "Dorms Management, We manage student housing.", 
        ["Mr. Samir"],
        "samir@ust.edu.eg"
    )
]

# Clubs routes
@browse_bp.route("/clubs")
def list_clubs():
    query = request.args.get("q", "")
    category = request.args.get("category", "")

    filtered = clubs
    if query:
        filtered = [c for c in filtered if query.lower() in c.name.lower()]
    if category:
        filtered = [c for c in filtered if c.category.lower() == category.lower()]

    return render_template("club_list.html", clubs=filtered)

@browse_bp.route("/clubs/<name>")
def club_detail(name):
    for c in clubs:
        if c.name == name:
            return render_template("club_details.html", club=c)
    return "Club not found", 404

# Offices routes
@browse_bp.route("/offices")
def list_offices():
    query = request.args.get("q", "")
    
    offices = repo.list_offices()
    filtered = offices

    if query:
        filtered = [o for o in filtered if query.lower() in o.name.lower()]

    return render_template("office_list.html", offices=filtered)

@browse_bp.route("/offices/<name>")
def office_detail(name):
    offices = repo.list_offices()
    for o in offices:
        if o.name == name:
            return render_template("office_details.html", office=o)
    return "Office not found", 404