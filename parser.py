# -*- coding: utf-8 -*-

from lxml import html
import json, os, codecs, itertools

hs = [h for h in os.listdir('./htmls') if h.endswith('html')]

for h in hs:
	with codecs.open('htmls/' + h, 'r', encoding='EUC-KR') as fp:
		text = fp.read()
	par = html.fromstring(text)
	img_src = [t.strip() for t in par.xpath("//img/@src")]
	names = [t.strip() for t in par.xpath("//font[@size='5']/b/text()")]
	desc_type = [t.strip()[:-1] for t in par.xpath("//td[@align='left']/font/b/text()")]
	token = desc_type[0]
	desc_desc = [t.strip() for t in par.xpath("//td[@align='left']/following-sibling::td/font/text()")]
	descs = zip(desc_type, desc_desc)
	descs = [list(x[1]) for x in itertools.groupby(descs, lambda x: x[0]==token) if not x[0]]
	table = zip(img_src, names, descs)
	parsed = [{
			'img_src' : t[0],
			'name' : t[1],
			'descs' : dict((tt[0], tt[1]) for tt in t[2])
		} for t in table]
	with open('parsed/' + h[:-5] + '.json', 'w') as fp:
		json.dump(parsed, fp)