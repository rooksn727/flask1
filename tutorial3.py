from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("tutorialinherit3.html", content="Testing")
    #we use the tutorial inehrirts3 html file whcih extends
    #base html file and shows both sections simultanously

if __name__ == "__main__":
    app.run(debug=True)