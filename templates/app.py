from flask import Flask
from controllers.admin_controller import admin_bp
from controllers.join_controller import join_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_bp)
    app.register_blueprint(join_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
