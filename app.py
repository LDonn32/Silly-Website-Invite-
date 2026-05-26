from flask import Flask, render_template, jsonify  # type: ignore[import]
import random

app = Flask(__name__)

funny_responses = [
    "Good. You better show up.",
    "Excellent choice. Dress fancy.",
    "You said yes? Bold of you.",
    "Perfect. Bring a naggin.",
    "Amazing. I’ll alert the paparazzi."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rsvp")
def rsvp():
    return jsonify({"message": random.choice(funny_responses)})

if __name__ == "__main__":
    app.run()
