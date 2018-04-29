# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:18:11 2018

@author: Hassan
"""


##module imports
from flask import Flask, request, jsonify, render_template, redirect, abort


app = Flask(__name__)



#default API description page
@app.route('/', methods=["GET", "POST"])
def route():
    ##return "Welcome to ROUTE web API App!"
    if request.method == "POST":
        print("post was called")
        attempted_username = request.form['username']
        ##attempted_password = request.form['password']
        
        if attempted_username == "admin":
            ##print(attempted_username +  "  " + attempted_password)
            return "this was a post"
        else:
            return "this was a post wihout a username and password"
        
    elif request.method == "GET":
        print("get method was called")
        return render_template("/main.html")
    
    else:
        print("method was neither a get nor a post")
        return render_template("/main.html")

#ip running on http://127.0.0.1:5000/
if __name__ == '__main__':
    print('running...')
    app.run(debug=True)