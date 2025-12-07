from flask import Blueprint, render_template, request, redirect, url_for, session
from repositories.message_repository import MessageRepository

message_bp = Blueprint("message", __name__, url_prefix="/messages")


@message_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if "user_email" not in session:
        session["user_email"] = "student@zewailcity.edu.eg"
    
    user = session["user_email"]

    if request.method == "POST":
        receiver = request.form["receiver"]
        content = request.form["content"]

        repo = MessageRepository()
        repo.send_message(user, receiver, content)

        return redirect(url_for("message.inbox"))

    return render_template("contact_form.html")


@message_bp.route("/inbox")
def inbox():
    if "user_email" not in session:
        session["user_email"] = "student@zewailcity.edu.eg"
    
    user = session["user_email"]
    
    repo = MessageRepository()
    
    msgs = repo.getMSG(user)
    notifs = repo.getNotif(user)

    return render_template("notifications.html", messages=msgs, notifications=notifs)