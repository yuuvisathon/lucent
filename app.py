import os

from flask import Flask, jsonify, request, abort
from datetime import datetime
from runner import runner

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/query', methods = ['POST'])
def query():

    os.environ['YUUVIS'] = "3f1d89b30d1a46aea1f21de3b4c7ef89"
    if not request.json:
        abort(400)
    return jsonify(runner(
        request.json['machine_id'],
        request.json['data_type']
    ))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

