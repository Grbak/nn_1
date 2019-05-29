import numpy
import math
from itertools import combinations

x = [[1, 0, 0, 0, 0],[1, 0, 0, 0, 1],[1, 0, 0, 1, 0],[1, 0, 0, 1, 1],[1, 0, 1, 0, 0],[1, 0, 1, 0, 1],[1, 0, 1, 1, 0],[1, 0, 1, 1, 1],[1, 1, 0, 0, 0],[1, 1, 0, 0, 1],[1, 1, 0, 1, 0],[1, 1, 0, 1, 1],[1, 1, 1, 0, 0],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0],[1, 1, 1, 1, 1]]
w = [0, 0, 0, 0, 0]
function = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nu = 0.5
E = 0

def our_function(s):
	if ((s[1]+s[2]+s[3])*(s[2]+s[3]+s[4])) > 0:
		return 1
	else:
		return 0

def heaviside_step_function(net):
	if net > 0:
		return 1
	else:
		return 0

def sigmoid_function(net):
	out = 0.5*(math.tanh(net)+1)
	if out >= 0.5:
		return 1
	elif out < 0.5:
		return 0

def null():
	for i in range (len(w)):
		w[i] = 0

def learning(x, w, activation):
	global E 
	age = 0
	while 1:
		E = 0
		print('Эпоха', age,':')
		for n in range(16):
			net = numpy.dot(x[n], w)

			if activation == 1:
				out = heaviside_step_function(net)

				for i in range(len(w)):
					print(w[i], end='  ')

				print('Выход:', round(out), end='  ')

				sygma = function[n] - out
				if sygma != 0:
					E += 1
					for i in range(len(w)):
						w[i] += nu*sygma*x[n][i]

				print('Суммарная ошибка равна', E,' - ', n+1,'-й шаг')


			if activation == 2:
				out = sigmoid_function(net)

				for i in range(len(w)):
					print(round(w[i], 2), end='  ')

				print('Выход:', round(out), end='  ')


				sygma = function[n] - out
				if sygma != 0:
					E += 1
					for i in range(len(w)):
						w[i] += nu*sygma*x[n][i]*0.5/(math.cosh(net)*math.cosh(net))

				print('Суммарная ошибка равна', E,' - ', n+1,'-й шаг')

		age += 1

		if E == 0:
			print('Чтобы обучить персептрон потребовалось', age-1, 'эпох.')
			break


def check(w, activation):
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
		k = 0
		while 1:
			e = 0
			print('Эпоха:', k)
			k += 1
			for g in range(count):
				net = numpy.dot(y[n][g], w)
				out = heaviside_step_function(net)

				for i in range(len(w)):
					print(w[i], end='  ')

				print('Выход:', round(out), end='  ')

				sygma = our_function(y[n][g]) - out
				if sygma != 0:
					e += 1
					for i in range(len(w)):
						w[i] += nu*sygma*y[n][g][i]

				print('Суммарная ошибка равна', e,' - ', g+1,'-й шаг')

			if e == 0:
				print('Проверяем данную выборку...')
				if check(w, 1):
					print(y[n], '- минимальная выборка, на которой персептрон сможет обучиться')
					exit(0)
				else:
					print('На этих наборах персептрон обучиться не может')
					break


def brute_2(y, count):
	for n in range(len(y)):
		null()
		print('Выборка:', y[n])
		k = 0
		while 1:
			e = 0
			print('Эпоха:', k)
			k += 1
			for g in range(count):
				net = numpy.dot(y[n][g], w)
				out = sigmoid_function(net)

				for i in range(len(w)):
					print(round(w[i], 2), end='  ')

				print('Выход:', round(out), end='  ')

				sygma = our_function(y[n][g]) - out
				if sygma != 0:
					e += 1
					for i in range(len(w)):
						w[i] += nu*sygma*y[n][g][i]*0.5/(math.cosh(net)*math.cosh(net))

				print('Суммарная ошибка равна', e,' - ', g+1,'-й шаг')

			if e == 0:
				print('Проверяем данную выборку...')
				if check(w, 1):
					print(y[n], '- минимальная выборка, на которой персептрон сможет обучиться')
					exit(0)
				else:
					print('На этих наборах персептрон обучиться не может')
					break


def brute_force(num):
	for index in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
		print('Выборка с количеством наборов, равным', index)
		set = list(combinations(x, index))

		if num == 1:
			brute_1(set, index)

		if num == 2:
			brute_2(set, index)


for index in range (len(x)):
	function[index] = our_function(x[index])


for i in range(len(x)):
	for j in [1, 2, 3, 4]:
		print(x[i][j], end=' ')
	print(' ', function[i])


while 1:
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
