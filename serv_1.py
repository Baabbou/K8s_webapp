#!/usr/bin/python3
from flask import Flask, redirect, render_template, request
from requests import post


app = Flask(__name__)
host_1 = {
    "ip": "0.0.0.0",
    "port": 8080
}
host_2 = {
    "ip": "127.0.0.1",
    "port": 8081
}


@app.route('/')
def index():
	return render_template("home1.html")


@app.route('/contact')
def contact():
    msg = request.args.get('msg')
    data = {'message': msg}
    post(f"http://{host_2['ip']}:{host_2['port']}/contact", data=data)  
    return redirect("/")

if __name__ == '__main__':
    app.run(host_1["ip"], host_1["port"], debug=False)
