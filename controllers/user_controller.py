from flask import Blueprint, render_template, request, redirect, url_for, session
from repositories.user_repository import UserRepository
from models.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_email" not in session:
        return redirect("/")
    
    original_email = session["user_email"]
    repo = UserRepository()

    if request.method == "POST":
        new_username = request.form["username"]
        new_email = request.form["email"]
        new_password = request.form["password"]
        
        current_user = repo.get_user_by_email(original_email)
        role = current_user.role
        
        updated_user = User(new_username, new_email, new_password, role)
        
        repo.update_user(updated_user, original_email)
        
        session["user_email"] = new_email
        
        return redirect(url_for("user.profile"))

    user_info = repo.get_user_by_email(original_email)
    
    return render_template("profile.html", user=user_info)