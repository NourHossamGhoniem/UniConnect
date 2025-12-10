from flask import Blueprint, render_template, request, redirect, url_for
from repositories.club_repository import ClubRepository

admin_bp = Blueprint("admin", __name__, template_folder="../templates/admin")
repo = ClubRepository()

@admin_bp.route("/admin")
def dashboard():
    clubs = repo.list_clubs()
    offices = repo.list_offices()
    return render_template("admin_dashboard.html", clubs=clubs, offices=offices)

@admin_bp.route("/admin/add", methods=["GET","POST"])
def add_entity():
    if request.method == "POST":
        entity_type = request.form.get("entity_type")
        name = request.form.get("name","").strip()
        description = request.form.get("description","").strip()
        category = request.form.get("category","").strip()
        if entity_type == "club":
            repo.create_club(name, description, category)
        else:
            repo.create_office(name, description)
        return redirect(url_for("admin.dashboard"))
    return render_template("add_edit_entity.html", mode="add")

@admin_bp.route("/admin/edit/<entity>/<int:entity_id>", methods=["GET","POST"])
def edit_entity(entity, entity_id):
    if entity not in ("club","office"):
        return redirect(url_for("admin.dashboard"))
    if request.method == "POST":
        name = request.form.get("name","").strip()
        description = request.form.get("description","").strip()
        category = request.form.get("category","").strip()
        if entity == "club":
            repo.update_club(entity_id, name, description, category)
        else:
            repo.update_office(entity_id, name, description)
        return redirect(url_for("admin.dashboard"))
    item = repo.get_club(entity_id) if entity=="club" else repo.get_office(entity_id)
    return render_template("add_edit_entity.html", mode="edit", entity=entity, item=item)

@admin_bp.route("/admin/delete/<entity>/<int:entity_id>", methods=["POST"])
def delete_entity(entity, entity_id):
    if entity == "club":
        repo.delete_club(entity_id)
    else:
        repo.delete_office(entity_id)
    return redirect(url_for("admin.dashboard"))

@admin_bp.route("/admin/add_member", methods=["POST"])
def add_member():
    entity = request.form.get("entity")
    entity_id = int(request.form.get("entity_id"))
    name = request.form.get("name")
    email = request.form.get("email")
    role = request.form.get("role")
    repo.add_member(entity, entity_id, name, email, role)
    return redirect(url_for("admin.dashboard"))

@admin_bp.route("/admin/assign_role", methods=["POST"])
def assign_role():
    entity = request.form.get("entity")
    entity_id = int(request.form.get("entity_id"))
    email = request.form.get("email")
    role = request.form.get("role")
    repo.assign_role(entity, entity_id, email, role)
    return redirect(url_for("admin.dashboard"))
