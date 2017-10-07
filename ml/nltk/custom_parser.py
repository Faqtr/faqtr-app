from __future__ import division
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
def process_text(text):
	Snowball = SnowballStemmer()
	try:
		x = re.findall(r'[0-9]+.in.[0-9]+', text)
		text = text.replace(x[0], str(eval(x[0].replace('in','/'))*100))
	except:
		pass
	try:
		x = re.findall(r'[0-9]+.of.[0-9]+', text)
		text = text.replace(x[0], str(eval(x[0].replace('of','/'))*100))
	except:
		pass
	try:
		x = re.findall(r'[0-9]+.out.of.[0-9]+', text)
		text = text.replace(x[0], str(eval(x[0].replace('out of','/'))*100))
	except:
		pass
	stop = set(stopwords.words('english'))
	text = ' '.join(Snowball.stem(i).encode('ascii', 'ignore') for i in text.lower().split() if i not in stop)
	return text