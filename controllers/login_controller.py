from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user_model import UserModel
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        user = UserModel.get_user_by_email(email)
        if user and check_password_hash(user["senha_hash"], senha):
            flash(f"Bem-vindo(a), {user['nome_completo']}!", "success")
            return redirect(url_for("login.login"))
        else:
            flash("Credenciais inválidas!", "danger")

    return render_template("login.html")
