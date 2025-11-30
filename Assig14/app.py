from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load HTML file safely using try-except (AI-refactored requirement)
def load_html():
    try:
        with open("index.html", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "<h2>Error: index.html file missing!</h2>"

@app.route("/", methods=["GET"])
def home():
    return render_template_string(load_html())

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    # Validate
    if username == "" or password == "":
        return "<h3>Error: Username or password cannot be empty!</h3>"

    # Print to terminal (Lab requirement)
    print("Logged in user:", username)

    return f"<h2>Login Successful!</h2><p>Welcome, {username}</p>"

if __name__ == "__main__":
    app.run(debug=True)
