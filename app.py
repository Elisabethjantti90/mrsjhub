from flask import Flask, render_template

app = Flask(__name__)

# Startsidan för hubben
@app.route("/")
def home():
    return render_template("index.html")

# Känslotracker
@app.route("/kanslotracker")
def kanslotracker():
    return render_template("kanslotracker.html")

# Reflektionsverktyg
@app.route("/pdf_journaling")
def pdf_journaling():
    return render_template("pdf_journaling.html")

if __name__ == "__main__":
    app.run(debug=True)