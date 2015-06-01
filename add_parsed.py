# -*- coding: utf-8 -*-

import json, os

js = [j for j in os.listdir('./parsed')]

a = []
for j in js:
	with open('parsed/' + j, 'r') as fp:
		a += json.load(fp)

with open('static/recipes.json', 'w') as fp:
	json.dump(a, fp)