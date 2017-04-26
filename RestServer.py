#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import Dictionary

app = Flask(__name__)


@app.route('/dictionary/<int:n>', methods=['GET'])
def get_nlength(n):
	return Dictionary.get_n_length_json(n)

if __name__ == '__main__':
	app.run(debug=True)