from flask import Flask, request, jsonify, render_template
import cohere
from dotenv import load_dotenv
import os
from utils.topic_filter import is_on_topic

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("⚠️ COHERE_API_KEY is missing in the .env file!")

app = Flask(__name__)

# Initialize Cohere client
co = cohere.Client(api_key=COHERE_API_KEY)
TOPIC = "car details"

# Track the number of greetings
greeting_count = 0

# List of common greetings
GREETINGS = ["hi", "hello", "hey", "greetings", "hi there", "hello there"]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # Serve the UI

@app.route("/chat", methods=["POST"])
def chat():
    global greeting_count
    try:
        data = request.get_json()
        user_question = data.get("question", "").strip().lower()  # Convert to lowercase for easier matching

        if not user_question:
            return jsonify({"error": "Question cannot be empty!"}), 400

        # Check if the message contains a greeting
        if any(greeting in user_question for greeting in GREETINGS):
            greeting_count += 1
            if greeting_count == 1:
                return jsonify({"answer": "Hello! I’m here to help with car details. What would you like to know about cars?"})
            else:
                return jsonify({"answer": f"Hello again! This is your greeting. I’m still here to assist with car details!"})

        # If not a greeting, check if it's on-topic (car-related)
        if is_on_topic(user_question):
            # Call Cohere API
            response = co.chat(
                message=user_question,
                model="command",  # Free tier model; use "command-r-plus" for paid
                preamble="You are an expert on car details. Provide accurate and concise answers about cars only.",
                max_tokens=150
            )
            answer = response.text.strip()
            return jsonify({"answer": answer})
        else:
            return jsonify({"answer": f"This model is only for {TOPIC}"}), 403

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
