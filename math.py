print('Это первая программа на python, следуйте указаниям программы')
print('Введите цифру больше нуля-->')
a=int(input())
print('Введите еще одну цифру больше нуля-->')
b=int(input())
if a == 0:
	print ('Ваше первое значение равно 0')
	exit()
if b == 0:
	print('Ваше второе значение равно 0')
	exit()
s=(2*(a+b))
print('Ваши цифры сложились и помножились на два, ответ равен = ', s )
