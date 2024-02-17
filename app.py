from flask import Flask, request, jsonify, render_template
from chat import get_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():

    text = request.get_json().get("message")
    response = get_response(text)

    message = {"answer": response}
    # Store chat data in MongoDB
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
