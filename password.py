chance = 3
while True:
	pwd = input('請輸入密碼: ')
	if pwd == 'a123456':
		print('登入成功')
		break
	elif pwd != 'a123456':
		print('密碼錯誤！ 還有', chance -1, '次機會')
		chance = chance - 1
		pwd = input('請輸入密碼: ')
		if pwd == 'a123456':
			print('登入成功')
			break
		elif pwd != 'a123456':
			print('密碼錯誤！ 還有', chance -1, '次機會')
			chance = chance - 1
			pwd = input('請輸入密碼: ')
			if pwd == 'a123456':
				print('登入成功')
				break
			elif pwd != 'a123456':
				print('密碼錯誤！ 還有', chance -1, '次機會')
				chance = chance - 1
				break
				if pwd == 'a123456':
					print('登入成功')
					break


