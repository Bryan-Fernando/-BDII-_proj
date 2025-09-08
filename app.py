from flask import Flask
from controllers.login_controller import login_bp
from dao.db import init_db

def create_app():
    app = Flask(__name__, template_folder="views", static_folder="static")
    app.config.from_object('config.Config')


    init_db() 
    app.register_blueprint(login_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
