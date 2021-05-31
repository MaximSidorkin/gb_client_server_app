'''
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
'''
print('Задание №1\n')

develop = 'разработка'
soket = 'сокет'
decor = 'декоратор'

print(str(develop), f'это тип {type(develop)}')
print(str(soket), f'это тип {type(soket)}')
print(str(decor), f'это тип {type(decor)}')

u_develop = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
u_soket = '\u0441\u043e\u043a\u0435\u0442'
u_decor = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print('\n')
print((u_develop), f'это тип {type(u_develop)}')
print((u_soket), f'это тип {type(u_soket)}')
print((u_decor), f'это тип {type(u_decor)}')

print('*'*100)


'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без 
преобразования в последовательность кодов (не используя методы encode и decode) 
и определить тип, содержимое и длину соответствующих переменных.
'''
print('Задание №2\n')
c = bytes(b'class')
f = bytes(b'function')
m = bytes(b'method')
print('Тип class == ', type(c), 'содержимое class == ', c, 'длинна class == ', len(c))
print('Тип class == ', type(f), 'содержимое class == ', f, 'длинна class == ', len(f))
print('Тип class == ', type(m), 'содержимое class == ', m, 'длинна class == ', len(m))
print('*'*100)
'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно 
записать в байтовом типе.
'''
print('Задание №3\n')

try:
    b_1 = b'attribute'
    print(b_1)
except:
    print('attribute - невозможно записать в байтовом типе.')

try:
    b_4 = b'type'
    print(b_4)
except:
    print('type - невозможно записать в байтовом типе.')

# try:
#     print(b'класс')
# except SyntaxError as e:
#     print(e, 'класс - невозможно записать в байтовом типе.')
#
# try:
#     print(b'функция')
# except(SyntaxError):
#     print('функция - невозможно записать в байтовом типе.')
# класс и функция вызывают SyntaxError

print('*'*100)

'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» 
из строкового представления в байтовое и выполнить обратное преобразование 
(используя методы encode и decode).
'''
print('Задание №4\n')
x = 'разработка'
y = 'администрирование'
z = 'protocol'
l = 'standard'

x_b = x.encode('utf-8')
print('из строкового представления в байтовое == ', x_b)
print('обратное преобразование == ', x_b.decode('utf-8'))
print('\n')
y_b = y.encode('utf-8')
print('из строкового представления в байтовое == ', y_b)
print('обратное преобразование == ', y_b.decode('utf-8'))
print('\n')
z_b = z.encode('utf-8')
print('из строкового представления в байтовое == ', z_b)
print('обратное преобразование == ', z_b.decode('utf-8'))
print('\n')
l_b = l.encode('utf-8')
print('из строкового представления в байтовое == ', l_b)
print('обратное преобразование == ', l_b.decode('utf-8'))
print('\n')
print('*'*100)


