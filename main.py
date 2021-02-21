from config import *
import os
from flask import Flask
from flask import flash, render_template, request, session, send_file, Markup, redirect
import json
from pathlib import Path

# NOTE: This program should be run as root or administrator to prevent file privilege problems

# ---validates config input----------------------------------------------
for item in accessible_directories["public"]:
    if not os.path.exists(item):
        print("\n !path or file '" + item + "' does not exist")
        accessible_directories["public"].remove(item)


for item in accessible_directories["protected"]["useraccess"]:
    if not os.path.exists(item[0]):
        print("\n !path or file '" + item[0] + "' does not exist")
        accessible_directories["protected"]["useraccess"].remove(item)
    if item[1] not in users.keys():
        print("\n !protected file or path '" + item[0] + "'. assigned user '" + item[1] + "' does not exist")
        accessible_directories["protected"]["useraccess"].remove(item)


# -----------------require user login-----------------------
app = Flask(__name__)


@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect("/login")
    else:
        return redirect("/filesystem")


@app.route("/filesystem")
def filesystem():
    return render_template("filesystem.html")


@app.route("/filesystem", methods=["POST"])
def get_directory():
    # return all the contents by user
    # if dir is specified step in the directory
    user_access = []
    public_access = []
    for user_item in accessible_directories["public"]:
        public_access.append(user_item)

    if session.get("logged_in"):
        for user_item in accessible_directories["protected"]["useraccess"]:
            if user_item[1] == session.get("user"):
                user_access.append(user_item[0])

    all_stuff = public_access + user_access
    # download the file selected
    if request.form:
        if os.path.isfile(request.form["dir"]):
            for item in all_stuff:
                if Path(item) in Path(request.form["dir"]).parents or request.form["dir"] == item:
                    try:
                        return send_file(request.form["dir"], as_attachment=True,
                                         attachment_filename=os.path.basename(request.form["dir"]))
                    except Exception as e:
                        return "Download failed! error: " + str(e)
                        print("Download failed! error: " + str(e))
                else:
                    return "404"
        # step in directory
        elif os.path.isdir(request.form["dir"]):
            for item in all_stuff:
                if Path(item) in Path(request.form["dir"]).parents or request.form["dir"] == item:
                    
                    try:
                        subs = os.walk(request.form["dir"])
                        for root, directories, files in subs:
                            return json.dumps(directories + files)
                    except Exception as e:
                        return "Unable to read directory! error: " + str(e)
                else:
                    return "404"
    return json.dumps(all_stuff)


@app.route("/login", methods=["POST"])
def login():
    if session.get("logged_in") or session.get("admin"):
        return redirect("/")
    if request.form['username'] in users:

        if users[request.form['username']] == request.form['password']:
            session['logged_in'] = True
            session['user'] = request.form['username']
            print("user \"" + request.form['username'] + "\" logged in. IP: " + request.remote_addr)
        else:
            flash('Login failed!')
    else:
        flash('Login failed!')
    return redirect("/")


@app.route("/login")
def login_get():
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["logged_in"] = False
    session["user"] = ""
    session["admin"] = False
    return home()

# run application
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(port=port, debug=True)
