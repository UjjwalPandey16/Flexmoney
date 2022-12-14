import requests
from flask import Flask, render_template,request,redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/index.html")
def hii ():
    return render_template('index.html')

@app.route("/form.html")
def form():
    return render_template('form.html')

@app.route("/form.html", methods=["POST","GET"])
def receive_data():
    errors = {}
    name = request.form["username"]
    age = int(request.form["age"])
    email = request.form["email"]
    timings = request.form["ftimings"]
    if age < 18:
        errors["age"] = ["Age should be greater than %d", age]

    if age > 65:
        errors["age"] = ["Age should be less than %d", age]
    if request.method == "POST":
        return redirect(url_for("user", usr=name, age=age, email=email,timings=timings,errors=errors))
    else:
        return render_template("form.html")

@app.route("/<usr>,<age>,<email>,<timings>")
def user(usr,age,email,timings):
    return render_template("details.html",usr=usr,age=age,email=email,timings=timings)

@app.route("/payment.html")
def completepayment():
    return render_template("complete.html")

if __name__ == "__main__":
    app.run(debug=True)
