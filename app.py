from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Add your Hugging Face API token here
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Get Hugging Face API key from environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not API_KEY:
    raise ValueError("No Hugging Face API key found. Set it in the .env file.")

API_URL = "https://api-inference.huggingface.co/models/yiyanghkust/finbert-tone"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    headline = request.form.get("headline")
    if not headline:
        return jsonify({"error": "Please provide a headline"})

    # Send request to Hugging Face API
    payload = {"inputs": headline}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return jsonify({"error": "Error communicating with Hugging Face API."})

    result = response.json()[0]
    print(response.json()[0])

    return response.json()[0]
    
    #return jsonify({"label": result['label'], "score": result['score']})

if __name__ == "__main__":
    app.run(debug=True)
