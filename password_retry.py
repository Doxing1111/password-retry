# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就打印 "登入成功"
# 如果不正確就打印 "密碼錯誤! 還有__次機會!"

password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 跳出迴圈
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('帳號已封鎖, 請洽客服')