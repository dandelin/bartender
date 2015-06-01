import json

with open('static/recipes.json', 'r') as fp:
	recipes = json.load(fp)

ingredient_key = recipes[0][u'descs'].keys()[0]

ingredient_strings = [recipe[u'descs'][ingredient_key] for recipe in recipes]

print ingredient_strings