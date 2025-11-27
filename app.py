from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/humble-pie")
def humble_pie():
    return "<h2>Humble Pie</h2><p>The sweetest way to say 'I told you so.'</p>"

if __name__ == "__main__":
    app.run(debug=True)
