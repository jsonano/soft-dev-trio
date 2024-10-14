# Victor Casado, Evan Chan, Jason Chao
# The Flying Mice
# 16 - Flask Sessions w/ Cookies
# SoftDev
# 2024-10-11
# Time spent: 2 hours

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32) # generates a random secret key for session

logins = {"victor" : "casado",
          "jason" : "chao",
          "evan" : "chan"}

@app.route('/')
def login():
    if 'username' in session:
        return redirect('/auth') # automatically redirect to /auth route if user is already logged in
    else:
        return render_template("login.html")

@app.route('/auth')
def auth_login():
    if 'username' in session:
        return render_template("home.html", user = session['username'])
    login = request.args
    username = login['username']
    password = login['password']
    # print(username)
    # print(password)
    if username in logins:
        if logins[username] == password:
            session['username'] = username
            return render_template("home.html", user = username)
        else:
            return redirect('/')
    else:
        return redirect('/') # redirect back to / route if username and/or password is incorrect



if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
