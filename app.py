<<<<<<< HEAD
from flask import Flask
from controllers.browse_controller import browse_bp

app = Flask(_name_)
app.register_blueprint(browse_bp)

@app.route("/")
def home():
    return """
    <h1>Welcome to UniConnect</h1>
    <p><a href='/clubs'>View Clubs</a></p>
    <p><a href='/offices'>View Offices</a></p>
    """

if _name_ == "_main_":
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
    
>>>>>>> d04b92f3ba8f7fd010fa29d23a8890a03cc7ec21
