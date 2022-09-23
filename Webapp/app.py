from flask import(Flask,jsonify,make_response,request,render_template,abort,make_response)
import urllib.request, json
import os


app = Flask(__name__)

Api_Url="http://api:5001/users/"

@app.route('/render')
def render():
    response = urllib.request.urlopen(Api_Url)
    data = response.read()
    dict = json.loads(data)
    return dict



@app.route('/')
def index():
        return render_template("index.html" )


@app.route('/about')
def about():
    return render_template("about.html" )


@app.route('/login')
def login():
     return render_template("login.html" )


@app.route('/register')
def register():
    return render_template("register.html" )


if __name__ == "__main__":
    app.run(debug=True)