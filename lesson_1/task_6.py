'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''

string = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as test_file:
    for i in string:
        test_file.write(i + '\n')

print('Кодировка файла по умолчанию.', test_file)

f = open("test_file.txt", "r", encoding="utf-8")
print(f.read())
f.close()