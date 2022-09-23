from flask import(Flask,jsonify,make_response,request,render_template,abort,make_response)
app = Flask(__name__)

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
    app.run()