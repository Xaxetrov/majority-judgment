from flask import Flask, request

from .vote import getVote, postVote

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        return postVote(request)
    else:
        return getVote(request)
