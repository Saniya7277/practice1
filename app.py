from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route('/')
def home():
    return jsonify({
        "message": "API is running successfully",
        "routes": ["/posts", "/comments", "/albums"]
    })


@app.route('/posts')
def posts():
    response = requests.get(f"{BASE_URL}/posts")
    return jsonify(response.json())


@app.route('/comments')
def comments():
    response = requests.get(f"{BASE_URL}/comments")
    return jsonify(response.json())


@app.route('/albums')
def albums():
    response = requests.get(f"{BASE_URL}/albums")
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
