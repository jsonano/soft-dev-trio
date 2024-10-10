# heading

from flask import Flask, render_template, request, session

app = Flask(__name__)

logins = {"victor" : "casado",
          "jason" : "chao",
          "evan" : "chan"}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/auth')
def auth_login():
    login = request.args
    print(login['username'])
    print(login['password'])
    username = login['username']
    password = login['password']
    if username in logins:
        if logins[username] == password:
            return render_template("home.html", user = username)
        else:
            return render_template("login.html")
    else:
        return render_template("login.html") # try to redirect back to route

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
