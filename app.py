from flask import Flask, render_template
import os

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    # Render the homepage template
    return render_template("home.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
