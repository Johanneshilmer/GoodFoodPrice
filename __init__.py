from flask import Flask, render_template, request

app = Flask(__name__) #Flask instance

@app.route("/", methods=["GET", "POST"])
def home(name):
    if request.method == "POST":
        name = request.form["nm"]
        return "Din text är", name
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)