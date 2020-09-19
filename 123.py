import json

with open(input("FIle:"), 'r') as f:
	file = json.load(f)

for i in file:
	with open(i['name'], 'w') as fileforwrite:
		fileforwrite.write(i['data'])

print('Unzip complete!')
input('Press enter for exit:')