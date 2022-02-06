password = 'ftfD35h#$%$fh'
treb_1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
treb_2 = '1234567890!@#$%^&*()-=_+'

if len(password) > 8:
    print('Пароль надежный')

else:
    print('Пароль не надежный')

for i in treb_1:
    if i in password:
        print('Пароль надежный x2')
        break
for i in treb_2:
    if i in password:
        print('Пароль надежный x3')
        break



