
from flask import Flask, render_template, request
from detector import analyze_email
from database import init_db, save_scan, get_scans

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        sender = request.form.get("sender", "")
        subject = request.form.get("subject", "")
        message = request.form.get("message", "")

  
        result = analyze_email(sender, subject, message)

        save_scan(
            sender,
            subject,
            result["score"],
            result["risk"]
        )


    return render_template("index.html", result=result)

@app.route("/history")
def history():
    scans = get_scans()
    return render_template("history.html", scans=scans)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
