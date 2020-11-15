def translate():
	"""Заменяет кириллицу на латинские буквы"""
	slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
	  'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
	  'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
	  'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
	  'ю':'u','я':'ja', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
	  'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
	  'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
	  'Ц':'C','Ч':'CZ','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
	  'Ю':'U','Я':'YA',',':'','?':'',' ':' ','~':'','!':'','@':'','#':'',
	  '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
	  ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
	  '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
	  'Є':'e', '—':'', ',':',', '.':'.'}
	print('Привет, набери текст для замены кириллицы на латинские буквы. Но только не наоборот!')
	print('Для выхода нажми "ВЫХОД"')
	while True:
		word = input('Текст для ввода: ')
		if word == 'ВЫХОД':
			break
		new_word = ''
		for k in word:
			if k in slovar:
				new_word += f'{slovar[k]}'
			else:
				print('\nКажется в тексте присутствуют символы, отличные от кириллицы, попробуй снова')
				break
		print(new_word)

translate()

