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