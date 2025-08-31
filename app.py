from flask import Flask
from controllers.login_controller import login_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(login_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
