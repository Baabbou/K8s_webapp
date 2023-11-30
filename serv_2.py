#!/usr/bin/python3
from flask import Flask, render_template,request


app = Flask(__name__)
BDD_messages = []
host_1 = {
    "ip": "127.0.0.1",
    "port": 8080
}
host_2 = {
    "ip": "0.0.0.0",
    "port": 8081
}


@app.route('/')
def home():
    global BDD_messages
    return render_template("contacted.html", messages=BDD_messages)


@app.route('/contact', methods=['POST'])
def contacted():
    global BDD_messages
    message = request.form.get('message')
    BDD_messages.append(message)
    return "Ok."

if __name__ == '__main__':
    app.run(host_2["ip"], host_2["port"], debug=False)
