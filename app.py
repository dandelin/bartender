# -*- coding: utf-8 -*-

from flask import Flask, make_response, render_template, request, redirect, Response
from flask.ext.restful import reqparse, abort, Resource, Api
import json, random, os

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('recipes', type=unicode)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static", "recipes.json")
recipes = json.load(open(json_url, 'r'))

@app.route('/')
def index():
    return render_template('index.html')

class return_recipes(Resource):
	def post(self):

		global recipes
		return recipes

	def get(self):

		global recipes
		return recipes
		
api.add_resource(return_recipes, '/api/recipes')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=11111)
