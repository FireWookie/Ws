import json
import csv
import os

main_dir = 'Data' # JSONs' folder
csvfile = open('1.1.csv', 'w+', encoding='utf-8', newline='')
writer = csv.writer(csvfile, delimiter=';')

# Write headers
writer.writerow(['title', 'about', 'rate', 'industries', 'date', 'text'])
for file_name in os.listdir(main_dir):
	with open(main_dir + '/' + file_name, 'r', encoding='utf-8') as f:
		data = json.load(f)
		title = str(f)
		title = title[title.find('/')+1:title.rfind('.')]
		# Get info fields
		info = data.get('info', {})
		if info:
			about = info.get('about', '')
			rate = info.get('rate', '')
			industries = ', '.join(info.get('industries', []))
		else:
			about = None
			rate = None
			industries = None

		# Loop through refs
		for ref in data.get('refs', []):
			if ref:
				text = ref[0]
				date = ref[1]
				day = date.get('day', '')
				month = date.get('month', '')
				time = date.get('time', '')
				date = ' '.join((day, month, time))
			else:
				text = None
				date = None

			row = [title, about, rate, industries, date, text]
			row = [(i.replace(';', ',') if isinstance(i, str) else i) for i in row]
			row = [(i.replace('\n', ' ') if isinstance(i, str) else i) for i in row]
			row = [(i.replace('\r', ' ') if isinstance(i, str) else i) for i in row]
			writer.writerow(row)
csvfile.close()
