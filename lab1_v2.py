import numpy
import math
from itertools import combinations

x = [[1, 0, 0, 0, 0],[1, 0, 0, 0, 1],[1, 0, 0, 1, 0],[1, 0, 0, 1, 1],[1, 0, 1, 0, 0],[1, 0, 1, 0, 1],[1, 0, 1, 1, 0],[1, 0, 1, 1, 1],[1, 1, 0, 0, 0],[1, 1, 0, 0, 1],[1, 1, 0, 1, 0],[1, 1, 0, 1, 1],[1, 1, 1, 0, 0],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0],[1, 1, 1, 1, 1]]
#Вектор x - множество различных входных значений. Соответсвтенно в каждом векторе первая единица - нейрон смещения
w = [0, 0, 0, 0, 0]
function = [0]*16 #Вектор в который мы положим значения булевой функции
nu = 0.5 #Норма обучения
E = 0 #Ошибка

def boolean_function(s): #Функция, высчитывающая значения булевой функции
	if ((s[1]+s[2]+s[3])*(s[2]+s[3]+s[4])) > 0:
		return 1
	else:
		return 0

def heaviside_step_function(net): #Пороговая функция активации
	if net > 0:
		return 1
	else:
		return 0

def sigmoid_function(net): #Сигмоидальная функция активации (гиперболический тангенс)
	out = 0.5*(math.tanh(net)+1)
	if out >= 0.5:
		return 1
	elif out < 0.5:
		return 0

def null(): #Функция, обнуляющая веса
	for i in range (len(w)):
		w[i] = 0

def learning(x, w, activation): #Функция, обучающая персептрон. activation - параметр, определяющий, какую функцую активации нужно использовать
	global E 
	age = 0 #Эпоха
	flag = 0 #Переменная, с помощью которой мы выходим из цикла 
	while flag == 0:
		E = 0
		print('Эпоха', age,':')
		for n in range(16):
			net = numpy.dot(x[n], w)

			if activation == 1:
				out = heaviside_step_function(net)

				for i in range(len(w)):
					print(w[i], end='  ')

				print('Выход:', round(out), end='  ')

				sigma = function[n] - out
				if sigma != 0:
					E += 1
					for i in range(len(w)):
						w[i] += nu*sigma*x[n][i]

				print('Суммарная ошибка равна', E,' - ', n+1,'-й шаг')


			if activation == 2:
				out = sigmoid_function(net)

				for i in range(len(w)):
					print(round(w[i], 2), end='  ')

				print('Выход:', round(out), end='  ')


				sigma = function[n] - out
				if sigma != 0:
					E += 1
					for i in range(len(w)):
						w[i] += nu*sigma*x[n][i]*0.5/(math.cos(net)*math.cos(net))

				print('Суммарная ошибка равна', E,' - ', n+1,'-й шаг')

		age += 1

		if E == 0:
			flag = 1

	print('Чтобы обучить персептрон потребовалось', age-1, 'эпох.')

def check(w, activation): #Функция, проверяющая, может ли выборка обучить персептрон так, чтобы он выдвал верный ответ на всех наборах
	global E 
	E = 0
	for n in range(len(x)):
		net = numpy.dot(x[n], w)

		if activation == 1:
			out = heaviside_step_function(net)

			if function[n] != out:
				return 0

		if activation == 2:
			out = sigmoid_function(net)

			if function[n] != out:
				return 0

	if E == 0:
		return 1
	else:
		return 0 

def brute_1(y, count): 
	for n in range(len(y)):
		null()
		print('Выборка:', y[n])
		age = 0
		flag = 0 #Переменная, с помощью которой мы выходим из цикла 
		while flag == 0:
			e = 0
			print('Эпоха:', age)
			age += 1
			for g in range(count):
				net = numpy.dot(y[n][g], w)
				out = heaviside_step_function(net)

				for i in range(len(w)):
					print(w[i], end='  ')

				print('Выход:', round(out), end='  ')

				sigma = boolean_function(y[n][g]) - out
				if sigma != 0:
					e += 1
					for i in range(len(w)):
						w[i] += nu*sigma*y[n][g][i]

				print('Суммарная ошибка равна', e,' - ', g+1,'-й шаг')

			if e == 0:
				print('Проверяем данную выборку...')
				if check(w, 1):
					print(y[n], '- минимальная выборка, на которой персептрон сможет обучиться') #В выводе первая единица в каждом наборе - нейрон смещения 
					exit(0)
				else:
					print('На этих наборах персептрон обучиться не может')
					flag = 1

def brute_2(y, count):
	for n in range(len(y)):
		null()
		print('Выборка:', y[n])
		age = 0
		flag = 0 #Переменная, с помощью которой мы выходим из цикла 
		while flag == 0:
			e = 0
			print('Эпоха:', age)
			age += 1
			for g in range(count):
				net = numpy.dot(y[n][g], w)
				out = sigmoid_function(net)

				for i in range(len(w)):
					print(round(w[i], 2), end='  ')

				print('Выход:', round(out), end='  ')

				sigma = boolean_function(y[n][g]) - out
				if sigma != 0:
					e += 1
					for i in range(len(w)):
						w[i] += nu*sigma*y[n][g][i]*0.5/(math.cos(net)*math.cos(net))

				print('Суммарная ошибка равна', e,' - ', g+1,'-й шаг')

			if e == 0:
				print('Проверяем данную выборку...')
				if check(w, 1):
					print(y[n], '- минимальная выборка, на которой персептрон сможет обучиться') #В выводе первая единица в каждом наборе - нейрон смещения 
					exit(0)
				else:
					print('На этих наборах персептрон обучиться не может')
					flag = 1

def brute_force(activation): #Функция, осуществляющая перебор всех возможных выборок. activation - параметр, определяющий, какую функцую активации нужно использовать
	for index in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		print('Выборка с количеством наборов, равным', index)
		set = list(combinations(x, index)) 

		if activation == 1:
			brute_1(set, index)

		if activation == 2:
			brute_2(set, index)

for index in range (len(x)):
	function[index] = boolean_function(x[index])

for i in range(len(x)):
	for j in [1, 2, 3, 4]:
		print(x[i][j], end=' ')
	print(' ', function[i])

#Для выполнения опредленной части лабораторной работы введите соответствующую цифру:
#1 - обучение с использованием всех комбинаций переменных с пороговой функцией активации
#2 - обучение с использованием всех комбинаций переменных с сигмоидальной функцией активации
#3 - обучение с использованием части возможных комбинаций переменных с пороговой функцией активации
#4 - обучение с использованием части возможных комбинаций переменных с сигмоидальной функцией активации
#5 - выход из программы

line = int(input())
if line == 1:
	null()
	learning(x, w, 1)
elif line == 2:
	null()
	learning(x, w, 2)
elif line == 3:
	null()
	brute_force(1)
elif line == 4:
	null()
	brute_force(2)
elif line == 5:
	exit(0)
