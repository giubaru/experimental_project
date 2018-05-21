'''
Templete 21/05/2018
author @gmarinel
'''

IMPORTED_FILE = 'datos.csv'
EXPORT_FILE = 'exported_'+IMPORTED_FILE
CODE_LEVEL = 0
VALUE_LEVEL = 1

_lines = []

with open(IMPORTED_FILE, 'r') as file:
	for i in file.readlines():
		line_raw = i.replace('\n','')
		line_refined = line_raw.split(";")
		_lines.append(line_refined)

	for position, line in enumerate(_lines):
		if line[VALUE_LEVEL] == '':
			new_value = [line[CODE_LEVEL], str(int(_lines[position-1][VALUE_LEVEL]) + 1)]
			_lines[position] = new_value
			

with open(EXPORT_FILE, 'a') as file_export:
	for position, line in enumerate(_lines):
		_lines[position] = ";".join(line)

	for position, line in enumerate(_lines):
		end_file = len(_lines)-1
		if position == end_file:
			file_export.write(line)
		else:
			file_export.write(line)
			file_export.write('\n')


'''
listo = [('a',1),('a','')]

for e, i in enumerate(listo):
	if i[1] == '':
		listo[e] = (i[0], listo[e-1][1]+1)
print(listo) 
'''