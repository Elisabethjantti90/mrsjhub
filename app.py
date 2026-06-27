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

# Vad händer?
@app.route("/vad_hander")
def vad_hander():
    return render_template("vad_hander.html")

    # Hur hjälper jag mig själv?
@app.route("/hur_hjalper")
def hur_hjalper():
    return render_template("hur_hjalper.html")

    # nervsystemscheck
@app.route("/nervsystem")
def nervsystem():
    return render_template("nervsystem.html")

if __name__ == "__main__":
    app.run(debug=True)