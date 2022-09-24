from flask import(Flask,jsonify,make_response,request,render_template,abort,make_response)
import urllib.request, json
import requests

app = Flask(__name__)

Api_Url="http://api:5001/users/"

@app.route('/render')
def render():
    response = urllib.request.urlopen(Api_Url)
    data = response.read()
    dict = json.loads(data)
    return dict



@app.route('/render1/<id>')
def render1(id):
    response = requests.get(Api_Url+id)
    return response.json()


 

@app.route('/')
def index():
        return render_template("index.html" )


@app.route('/about')
def about():
    return render_template("about.html" )


@app.route('/login')
def login():
     return render_template("login.html" )


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        json_user={"username": username , "password": password }
        requests.post(Api_Url+"add", json =json_user)
        return render_template("register.html")
    else:
        return "Beklenmedik web istegi"

    


if __name__ == "__main__":
    app.run(debug=True)