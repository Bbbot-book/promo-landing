@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Orange Sky</title>
        <style>
            body { font-family: Arial, sans-serif; background:#f9f9f9; text-align:center; padding:40px; }
            h1 { color:#333; margin-bottom:10px; }
            h2 { color:#444; margin-top:30px; }
            p { font-size:18px; color:#555; max-width:700px; margin:auto; line-height:1.6; }
            .services { text-align:left; max-width:700px; margin:30px auto; }
            .services strong { color:#222; }
            button { background:#25D366; color:white; border:none; padding:15px 25px; font-size:18px; border-radius:8px; cursor:pointer; margin-top:20px; }
            button:hover { background:#128C7E; }
        </style>
    </head>
    <body>
        <h1>Orange Sky</h1>
        <h2>Product Sourcing & Shipping</h2>
        <p>
            Thank you for visiting Orange Sky today. We make sourcing simple: from everyday items to building materials,
            furniture, machinery, and battery storage systems — you name it, we find it. No more wasting time checking endless
            suppliers; we handle the hard work for you and show you the possibilities.
        </p>
        <div class="services">
            <h2>Services</h2>
            <p><strong>Sourcing Request:</strong> Share what you need, and we’ll do the job. We find reliable suppliers, negotiate on your behalf, and secure the best deal.</p>
            <p><strong>Logistics:</strong> We connect you with trusted shipping partners to ensure your goods are delivered safely and on time.</p>
            <p><strong>Pay & Place Order:</strong> With crypto payments accepted, transactions are faster and easier.</p>
        </div>
        <h2>Contact Us</h2>
        <p>Direct WhatsApp support — one click away.</p>
        <a href="https://wa.me/9607720080" target="_blank">
            <button>Chat on WhatsApp</button>
        </a>
        <p>📞 +9667720980<br>📧 latheefmohamed124@gmail.com<br>▶️ YouTube: @OrangeSkydeals</p>
    </body>
    </html>
    """
