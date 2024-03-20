ask(__name__)
translatfrom flask import Flask, render_template, request, redirect, url_for
from googletrans import Translator

app = Flor = Translator()

@app.route("/", methods=["GET", "POST"])
def translate_text():
    if request.method == "POST":
        text = request.form.get("text")
        src_lang = request.form.get("src_lang")
        dest_lang = request.form.get("dest_lang")

        # Translate the text
        translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text

        return render_template("index.html", translated_text=translated_text)

    return render_template("index.html", translated_text=None)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

# Define a route to handle the login form submission
@app.route("/login_submit", methods=["POST"])
def login_submit():
    # Handle login logic here, for example, checking username and password
    # If login is successful, you can redirect to the /index page
    return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
