from flask import Flask, render_template, redirect, url_for
from controllers.auth_controller import auth_bp
from controllers.admin_controller import admin_bp
from controllers.browse_controller import browse_bp
from controllers.join_controller import join_bp
from controllers.message_controller import message_bp

app = Flask(__name__)
app.secret_key = 'uniconnect_secret_key_123'

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(browse_bp)
app.register_blueprint(join_bp)
app.register_blueprint(message_bp)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)