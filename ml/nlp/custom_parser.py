from __future__ import division
import re
from gensim.parsing.porter import PorterStemmer
def process_text(text):
	stem = PorterStemmer()
	try:
		x = re.findall(r'[0-9]+.in.[0-9]+', text)
		text = text.replace(x[0], str(eval(x[0].replace('in','/'))*100)+'%')
	except:
		pass
	try:
		x = re.findall(r'[0-9]+.of.[0-9]+', text)
		text = text.replace(x[0], str(eval(x[0].replace('of','/'))*100)+'%')
	except:
		pass
	try:
		x = re.findall(r'[0-9]+.out.of.[0-9]+', text)
		text = text.replace(x[0], str(eval(x[0].replace('out of','/'))*100)+'%')
	except:
		pass
	return ' '.join(stem.stem(i) for i in text.lower().split())