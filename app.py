from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("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")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_msg}]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
