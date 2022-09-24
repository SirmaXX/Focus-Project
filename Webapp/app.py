from flask import(Flask,request,render_template,session,url_for,redirect)
import urllib.request, json
import requests

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


Api_Url="http://api:5001/users/"

@app.route('/render')
def render():
    """ üyeleri listelenmesi için örnek request"""
    response = urllib.request.urlopen(Api_Url)
    data = response.read()
    dict = json.loads(data)
    return dict



@app.route('/render1/<id>')
def render1(id):
    """ tekil üyeye ait"""
    response = requests.get(Api_Url+id)
    return response.json()


 

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    """ anasayfaya ait fonksiyon"""
    if request.method == "GET": 
        if 'username' in session:
          username = session['username']
          return render_template("index.html" )
        return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"
    else:
        return render_template("login.html" )
        


@app.route('/about')
def about():
     """ hakkında sayfasına ait fonksiyon"""
     return render_template("about.html" )


@app.route('/login', methods=["GET", "POST"])
def login():
    """ giriş ait fonksiyon"""
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session['username'] = request.form['username']
        json_user={"username": username , "password": password }
        checklogin=requests.post(Api_Url+"login", json =json_user)
        # checkvar=json.loads( checklogin.text)
        if (checklogin.text =="true"):
            return render_template("index.html")
        else:
             return "yanlis giris"
    else:
         return "Beklenmedik web istegi"






@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))






@app.route('/register', methods=["GET", "POST"])
def register():
    """ kayıt sayfasına ait fonksiyon """
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