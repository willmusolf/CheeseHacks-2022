from flask import Flask, jsonify, Response
from flask_cors import CORS
from flask import request

from generate_degrees import generate_degrees
from parse_transcript import parse_transcript
from scrape import scrape

DEBUG = True

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def hello():
    return 'hi'


@app.route('/update', methods=['GET'])
def update():
    return scrape()


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    if 'pdf' not in file.filename:
        return jsonify({'status': 'not a pdf'})

    file.save('transcript.pdf')

    courses = parse_transcript()

    if isinstance(courses, Response):
        return courses

    return generate_degrees(courses)


if __name__ == '__main__':
    app.run()
