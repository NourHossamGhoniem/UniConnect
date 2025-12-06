# controllers/auth_controller.py

from flask import Blueprint, render_template, request, redirect, session
from repositories.user_repository import UserRepository
from models.user import User

print("Controllers loaded")

auth_bp = Blueprint("auth", __name__, url_prefix="/")
repo = UserRepository()

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if not email.endswith("@ust.edu.eg"):
            return "Email must be university email (@ust.edu.eg)"

        if repo.get_user_by_email(email):
            return "Email already exists"

        new_user = User(username, email, password)
        repo.add_user(new_user)
        return redirect("/login")

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = repo.get_user_by_email(email)
        if user and user.password == password:
            session["user_email"] = user.email
            return redirect("/profile")

        return "Invalid credentials"

    return render_template("login.html")

@auth_bp.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_email" not in session:
        return redirect("/login")

    user = repo.get_user_by_email(session["user_email"])

    if request.method == "POST":
        user.username = request.form["username"]
        repo.update_user(user)
        return "Profile updated!"

    return render_template("profile.html", user=user)

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
