country = input('請問你的國家是？')
age = input('請問你的年齡')
age = int(age)
if country == '臺灣' or country == '中華民國' or country == '台灣':
	if age >= 18:
		print('你可以考取駕照')
	else:
		print('你不能考取駕照')
elif country == '美國' or country == 'American' or country =='usa':
	if age >= 16:
		print('你可以考取駕照') 
	else:
		print('你不能考取駕照')
else:
	print('你上網查詢')				