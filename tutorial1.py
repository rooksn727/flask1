from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello world<p>"

@app.route("/<name>") #takes the /<name> as a variable and displays it afterwards
def user(name):
    return f"hello {name}"

@app.route("/admin/") #redirects url admin to the home page
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()