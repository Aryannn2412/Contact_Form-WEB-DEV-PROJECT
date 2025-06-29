from flask import Flask, request, jsonify, render_template
from filter import is_spam

app = Flask(__name__)

# Home route to serve the contact form
@app.route('/')
def home():
    return render_template('index.html')

# API route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({"status": "error", "reason": "Missing name or message"}), 400

    if is_spam(message):
        return jsonify({"status": "rejected", "reason": "Spam detected"}), 400

    return jsonify({"status": "accepted", "name": name, "message": message}), 200

if __name__ == '__main__':
    app.run(debug=True)
