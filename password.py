# password = 'a123456'
# chance = 3
# while True:
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功')
# 		break
# 	elif pwd != password:
# 		chance = chance - 1
# 		print('密碼錯誤！ 還有', chance, '次機會')
# 		pwd = input('請輸入密碼: ')
# 		if pwd == password:
# 			print('登入成功')
# 			break
# 		elif pwd != password:
# 			chance = chance - 1
# 			print('密碼錯誤！ 還有', chance, '次機會')
# 			pwd = input('請輸入密碼: ')
# 			if pwd == password:
# 				print('登入成功')
# 				break
# 			elif pwd != password:
# 				chance = chance - 1
# 				print('密碼錯誤！ 還有', chance, '次機會')
# 				break
# 				if pwd == password:
# 					print('登入成功')
# 					break

password = 'a123456'
chance = 3
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		chance = chance - 1
		print('密碼錯誤！ 還有', chance, '次機會')
		if chance == 0:
			break