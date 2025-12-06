<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask
from controllers.browse_controller import browse_bp

app = Flask(_name_)
app.register_blueprint(browse_bp)
=======
print("Starting app...")

from flask import Flask
from controllers.auth_controller import auth_bp

app = Flask(__name__)
app.secret_key = "secret123"
app.register_blueprint(auth_bp)
>>>>>>> 1c66b010ebcc87cb298247f18e13d7efc0b6cce8

@app.route("/")
def home():
    return """
<<<<<<< HEAD
    <h1>Welcome to UniConnect</h1>
    <p><a href='/clubs'>View Clubs</a></p>
    <p><a href='/offices'>View Offices</a></p>
    """

if _name_ == "_main_":
=======
    <h1>Welcome</h1>
    <p><a href='/login'>Login</a></p>
    <p><a href='/register'>Register</a></p>
    """

if __name__ == "__main__":
>>>>>>> 1c66b010ebcc87cb298247f18e13d7efc0b6cce8
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
    
<<<<<<< HEAD
>>>>>>> d04b92f3ba8f7fd010fa29d23a8890a03cc7ec21
=======
>>>>>>> a9feda36baf6ec821e00362042a6484b3eb185b6
>>>>>>> 1c66b010ebcc87cb298247f18e13d7efc0b6cce8
