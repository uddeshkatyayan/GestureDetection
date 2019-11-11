import sys
import glob

text = ''

files = glob.glob('*.jpg')
for line in files:
	if "right" in line:
		label = '1'
	elif "left" in line:
		label = '2'
	elif "center" in line or "centre" in line:
		label = '3'
	text += '"'+line+'", '+label+'\n'
with open('labels.csv','w+') as f:
	f.write(text)
