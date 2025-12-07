from flask import Blueprint, render_template, request

from models.club import Club
from models.office import Office

browse_bp = Blueprint("browse", _name_)


clubs = [
    Club("IEEE", "Robotics club", "Academic", ["Ali", "Omar"], "ieee@zewailcity.edu.eg"),
    Club("Drama", "Acting & Theatre", "Social", ["Lina", "Sara"], "drama@zewailcity.edu.eg")
]

offices = [
    Office("CATS", "Career Advising Office", ["Dr. Maha"], "cats@zewailcity.edu.eg"),
    Office("Housing", "Dorms Management", ["Mr. Samir"], "housing@zewailcity.edu.eg")
]


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
            return render_template("club_detail.html", club=c)
    return "Club not found", 404


@browse_bp.route("/offices")
def list_offices():
    return render_template("office_list.html", offices=offices)

@browse_bp.route("/offices/<name>")
def office_detail(name):
    for o in offices:
        if o.name == name:
            return render_template("office_detail.html", office=o)
    return "Office not found", 404
