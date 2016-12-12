import os, re, codecs

def set_weights(w0, w1, w2, w3, w4):
	return [w0, w1, w2, w3, w4]

def collect_data():
	titles=[]
	texts=[]
	for i in os.listdir('.'):
		if 'txt' in i:
			f=codecs.open(i, 'r')
			txt=f.read()
			f.close()
			titles.append(i)
			texts.append(txt)
	return titles, texts

def check_features(title, text):
	x3=card_feature(text)
	x1=date_feature(text)
	x2=title_feature(title)
	x4=bio_feature(text)
	return [x1, x2, x3, x4]

def date_feature(text):
	feat=re.search('\{\{ДР\|\d+\|\d+\|\d+\}\}', text)
	if feat is not None:
		return 1
	elif 'одился в' in text or 'ата рождения' in text:
		return 1
	return 0

def card_feature(text):
	feat=re.search('\|имя: +=\w', text)
	if feat is not None:
		return 1
	return 0

def title_feature(title):
	if ',' in title:
		return 1
	return 0

def bio_feature(text):
	if '== Биография ==' in text:
		return 1
	return 0

def classify():
	titles, texts=collect_data()
	for i in range(len(titles)):
		x=check_features(titles[i], texts[i])
		w=set_weights(-0.5, 0.5, 1, 1, 1)
		w0=w[0]
		w=w[1:]
		if w0 + sum(w[n] * x[n] for n in range(4)) > 0:
			yield titles[i]+' person'
		else:
			yield titles[i]+' not person'

for i in classify():
	print(i)
