from flask import Flask, redirect, session
from controllers.message_controller import message_bp

app = Flask(__name__)
app.secret_key = "secret_key"

app.register_blueprint(message_bp)

@app.route('/')
def home():
    return redirect('/messages/inbox')

if __name__ == '__main__':
    app.run(debug=True)