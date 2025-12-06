<<<<<<< HEAD
print("Starting app...")

from flask import Flask
from controllers.auth_controller import auth_bp

app = Flask(__name__)
app.secret_key = "secret123"
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return """
    <h1>Welcome</h1>
    <p><a href='/login'>Login</a></p>
    <p><a href='/register'>Register</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
    
>>>>>>> a9feda36baf6ec821e00362042a6484b3eb185b6
