# -*- coding: utf-8 -*-

from lxml import html
import json, os, codecs, itertools

hs = [h for h in os.listdir('./htmls') if h.endswith('html')]

for h in hs:
	with codecs.open('htmls/' + h, 'r', encoding='EUC-KR') as fp:
		text = fp.read()
	par = html.fromstring(text)
	img_src = [t.strip()[2:] for t in par.xpath("//img/@src")]
	names = [t.strip() for t in par.xpath("//font[@size='5']/b/text()")]
	desc_group = par.xpath("/html/body/table/tbody/tr/td/table[position() mod 2 = 0]")
	descs = [zip([t.strip()[:-1] for t in dg.xpath(".//td[@align='left']/font/b/text()")], [t.strip() for t in dg.xpath(".//td[@align='left']/following-sibling::td/font/text()")]) for dg in desc_group]
	table = zip(img_src, names, descs)
	parsed = [{
			'img_src' : t[0],
			'name' : t[1],
			'descs' : dict((tt, td) for tt, td in t[2])
		} for t in table]
	with open('parsed/' + h[:-5] + '.json', 'w') as fp:
		json.dump(parsed, fp)