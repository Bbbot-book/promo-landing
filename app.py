from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Orange Sky</title>
        <style>
            body { font-family: Arial, sans-serif; background:#f0f2f5; text-align:center; padding:50px; }
            h1 { color:#222; margin-bottom:10px; }
            p { font-size:18px; color:#555; }
            .menu { margin-top:30px; }
            a { display:inline-block; margin:15px; font-size:18px; color:#25D366; text-decoration:none; padding:10px 20px; border:1px solid #25D366; border-radius:6px; }
            a:hover { background:#25D366; color:white; }
        </style>
    </head>
    <body>
        <h1>Orange Sky</h1>
        <p>Quality products with direct WhatsApp support.</p>
        <div class="menu">
            <a href="/patio-swing">Patio Swing</a>
        </div>
    </body>
    </html>
    """

@app.route("/patio-swing")
def patio_swing():
    return """
    <html>
    <head>
        <title>Patio Swing - Orange Sky</title>
        <style>
            body { font-family: Arial, sans-serif; background:#f9f9f9; text-align:center; padding:50px; }
            h1 { color:#333; }
            p { font-size:18px; color:#555; }
            button { background:#25D366; color:white; border:none; padding:15px 25px; font-size:18px; border-radius:8px; cursor:pointer; }
            button:hover { background:#128C7E; }
            .card { background:white; padding:30px; border-radius:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1); display:inline-block; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Patio Swing</h1>
            <img src="https://via.placeholder.com/400x250" alt="Patio Swing" style="border-radius:8px; margin-bottom:20px;">
            <p>Comfortable outdoor swing for your garden.<br>
            Durable steel frame, weather‑resistant cushions.</p>
            <a href="https://wa.me/9607720080" target="_blank">
                <button>Chat on WhatsApp</button>
            </a>
            <p style="margin-top:20px; font-size:14px; color:#888;">Secure purchase • Direct chat support</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
