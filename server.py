from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojo/new')
def dojo():
    print "created a ninja"
    name = request.form["name"]
    power = request.form["power"]
    return render_template("dojos.html")
app.run(debug=True)
