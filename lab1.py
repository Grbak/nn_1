import numpy as np
from itertools import combinations
from itertools import permutations
import copy

x1 = ([1, 0, 0, 0, 0])
x2 = ([1, 0, 0, 0, 1])
x3 = ([1, 0, 0, 1, 0])
x4 = ([1, 0, 0, 1, 1])
x5 = ([1, 0, 1, 0, 0])
x6 = ([1, 0, 1, 0, 1])
x7 = ([1, 0, 1, 1, 0])
x8 = ([1, 0, 1, 1, 1])
x9 = ([1, 1, 0, 0, 0])
x10 = ([1, 1, 0, 0, 1])
x11 = ([1, 1, 0, 1, 0])
x12 = ([1, 1, 0, 1, 1])
x13 = ([1, 1, 1, 0, 0])
x14 = ([1, 1, 1, 0, 1])
x15 = ([1, 1, 1, 1, 0])
x16 = ([1, 1, 1, 1, 1])
x = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16]

class Niro(object):
    n = 0.3
    t = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    d = {'[1, 0, 0, 0, 0]': 1, '[1, 0, 0, 0, 1]': 1, '[1, 0, 0, 1, 0]': 1, '[1, 0, 0, 1, 1]': 1, '[1, 0, 1, 0, 0]':0, '[1, 0, 1, 0, 1]':1, '[1, 0, 1, 1, 0]': 1, '[1, 0, 1, 1, 1]':1, '[1, 1, 0, 0, 0]':0,'[1, 1, 0, 0, 1]':1,'[1, 1, 0, 1, 0]': 1,'[1, 1, 0, 1, 1]':1,'[1, 1, 1, 0, 0]':0, '[1, 1, 1, 0, 1]': 1, '[1, 1, 1, 1, 0]':1,'[1, 1, 1, 1, 1]':1}   
    def __init__(self, x, i):
        self.count = 0
        self.idol = i
        self.array = x
        self.weight = [0, 0, 0, 0, 0]
        print("-------- Программа начала работу --------")
    
    def activation_function(self, net):
        if (net >= 0):
            return 1
        else:
            return 0
    def activation_func_2(self, net):
        return 1 if 0.5 * (net / (1+ abs(net)) + 1) >= 0.5 else 0
    
    def d_func_2(self, net):
        f = 0.5 * (net / (1 + abs(net)) + 1)
        return 0.5 / ((1 + abs(f)) **2)
    
    def check(self, w):
        self.E = 0
        print("-----------------РАБОТА ТЕСТОВОЙ ФУНКЦИИ----------------------")
        for j in range(len(self.idol)):
            print("На вход:", self.idol[j])
            print(" ")
            print("Вектор весов:", w)
            print(" ")
            self.net = np.dot(self.idol[j], w)
            print("net = ", self.idol[j], " * ", w, " = ", self.net)
            if (self.activation_function(self.net)):
                self.out = 1
                self.Fnet = 1
                self.y = 1
                print("Реальный выход:", self.y)
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    print("Набор не подходит.")
            else:
                print("Реальный выход: 0")
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.y = 0
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    print("Набор не подходит.")
        if (self.E == 0):
           return 1
    def check_sig(self, w):
        self.E = 0
        print("-----------------РАБОТА ТЕСТОВОЙ ФУНКЦИИ----------------------")
        for j in range(len(self.idol)):
            print("На вход:", self.idol[j])
            print(" ")
            a = copy.copy(w)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print("Вектор весов:", a)
            print(" ")
            self.net = np.dot(self.idol[j], w)
            net_out = round(copy.copy(self.net),3)
            print("net = ", self.idol[j], " * ", a, " = ", net_out)
            if (self.activation_func_2(self.net)):
                self.out = 1
                self.Fnet = 1
                self.y = 1
                print("------------------------------------Реальный выход:", self.y)
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    print("Набор не подходит.")
            else:
                print("------------------------------------Реальный выход: 0")
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.y = 0
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    print("Набор не подходит.")
        if (self.E == 0):
           return 1
        
    def nettt(self):
        self.E = 0
        print("_____________ЭПОХА_____________:", self.count)
        print(" ")
        self.count += 1
        for j in range(len(self.array)):
            print("На вход:", self.array[j])
            print(" ")
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print("Вектор весов:", a)
            print(" ")
            self.net = np.dot(self.array[j], self.weight)
            net_out = round(copy.copy(self.net),3)
            print("net = ", self.array[j], " * ", a, " = ", net_out)
            if (self.activation_function(self.net)):
                self.out = 1
                self.Fnet = 1
                self.y = 1
                print("Реальный выход:", self.y)
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i]
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
            else:
                print("Реальный выход: 0")
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.y = 0
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i]
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
        print("Суммарная ошибка:", self.E)
        if (self.E == 0):
            print("Программа закончила работу:")
            print("Колличество эпох: :", self.count - 1)
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print("Конечный вектор весов: ", a)
            exit(0)
        print(" ")
        print(" ")
        print(" ")

    def nettt_2(self):
        self.E = 0
        print("_____________ЭПОХА____________:", self.count)
        print(" ")
        self.count += 1
        for j in range(len(self.array)):
            print("На вход:", self.array[j])
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print(" ")
            print("Вектор весов:", a)
            print(" ")
            self.net = np.dot(self.array[j] , self.weight)
            net_out = round(copy.copy(self.net),3)
            print("net = ", self.array[j], " * ", a, " = ", net_out)
            if (self.activation_func_2(self.net)):
                self.out = 1
                self.y = 1
                print("Реальный выход:", self.y)
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i] * self.d_func_2(self.net)
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " * ", self.d_func_2(self.net), " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
            else:
                self.y = 0
                print("Реальный выход: ", self.y)
                print(" ")
                print("Целевой выход:", self.t[j])
                print(" ")
                self.Error = self.t[j] - self.y
                print("Error = ", self.t[j], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i] * self.d_func_2(self.net)
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " * ", self.d_func_2(self.net), " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
        print("Суммарная ошибка:", self.E)
        if (self.E == 0):
            print("Программа закончила работу:")
            print("Колличество эпох: :", self.count - 1)
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print("Конечный вектор весов: ", a)
            exit(0)
        print(" ")
        print(" ")
        print(" ")

    def brut(self):
        self.E = 0
        print("--------------------Обучение минимального набора------------------", self.array)
        print("_____________ЭПОХА____________:", self.count)
        print(" ")
        self.count += 1
        for j in range(len(self.array)):
            print("На вход:", self.array[j])
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print(" ")
            print("Вектор весов:", a)
            print(" ")
            self.net = np.dot(self.array[j], self.weight)
            net_out = round(copy.copy(self.net),3)
            print("net = ", self.array[j], " * ", self.weight, " = ", net_out)
            if (self.activation_function(self.net)):
                self.out = 1
                self.Fnet = 1
                self.y = 1
                print("------------------------------------Реальный выход:", self.y)
                print(" ")
                kk = "".join(str(self.array[j]))
                print("Целевой выход:", self.d[kk])
                print(" ")
                self.Error = self.d[kk] - self.y
                print("Error = ", self.d[kk], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i]
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
            else:
                print("Реальный выход: 0")
                print(" ")
                kk = "".join(str(self.array[j]))
                print("Целевой выход:", self.d[kk])
                print(" ")
                self.y = 0
                self.Error = self.d[kk] - self.y
                print("Error = ", self.d[kk], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i]
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
        print("Суммарная ошибка:", self.E)
        print(" ")
        print(" ")
        print(" ")
        if (self.E ==  0):
            print("Проыерка минимального набора:", self.array)
            print("Вектор весов:",  self.weight)
            if (self.check(self.weight)):
                print("Программа закончила работу:")
                print("Колличество эпох: :", self.count - 1)
                print("Минимальный набор", self.array)
                a = copy.copy(self.weight)
                for item in range(len(a)):
                    a[item] = round(a[item],3)
                print("Конечный вектор весов: ", a)
                exit(0)
    def brut_sig(self):
        self.E = 0
        print("--------------------Обучение минимального набора------------------", self.array)
        print("_____________ЭПОХА____________:", self.count)
        print(" ")
        self.count += 1
        for j in range(len(self.array)):
            print("На вход:", self.array[j])
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print(" ")
            print("Вектор весов:", a)
            print(" ")
            self.net = np.dot(self.array[j], self.weight)
            net_out = round(copy.copy(self.net),3)
            print("net = ", self.array[j], " * ", self.weight, " = ", net_out)
            if (self.activation_func_2(self.net)):
                self.out = 1
                self.Fnet = 1
                self.y = 1
                print("Реальный выход:", self.y)
                print(" ")
                kk = "".join(str(self.array[j]))
                print("Целевой выход:", self.d[kk])
                print(" ")
                self.Error = self.d[kk] - self.y
                print("Error = ", self.d[kk], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i] * self.d_func_2(self.net)
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " * ", self.d_func_2(self.net), " = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
            else:
                print("Реальный выход: 0")
                print(" ")
                kk = "".join(str(self.array[j]))
                print("Целевой выход:", self.d[kk])
                print(" ")
                self.y = 0
                self.Error = self.d[kk] - self.y
                print("Error = ", self.d[kk], " - " ,self.y, " = ", self.Error)
                print(" ")
                if (self.Error != 0):
                    self.E +=1
                    for i in range(5):
                        self.dW = self.n * self.Error * self.array[j][i] * self.d_func_2(self.net)
                        dW_out = round(copy.copy(self.dW),3)
                        print("Изменение W[",i,"] = ", self.n," * ", self.Error, " * ", self.array[j][i], " * ", self.d_func_2(self.net)," = ", dW_out)
                        self.weight[i] += self.dW
                        a = round(copy.copy(self.weight[i]),3)
                        print("Вес W[",i,"] = ", a)
        print("Суммарная ошибка:", self.E)
        print(" ")
        print(" ")
        print(" ")
        if (self.E ==  0):
            print("Проверка минимального набора:", self.array)
            a = copy.copy(self.weight)
            for item in range(len(a)):
                a[item] = round(a[item],3)
            print("Вектор весов:",  a)
            if (self.check_sig(self.weight)):
                print("Программа закончила работу:")
                print("Колличество эпох: :", self.count - 1)
                print("Минимальный набор", self.array)
                a = copy.copy(self.weight)
                for item in range(len(a)):
                    a[item] = round(a[item],3)
                print("Конечный вектор весов: ", a)
                exit(0)

def brutforce(x,i):
    v = i
    count = 1
    while (count < 17):
        for item in combinations( x, count):
            y = list(item)
            a = Niro(y, x)
            if (v == 1):
                for i in range(6):
                    a.brut()
            elif (v == 2):
                for i in range(6):
                    a.brut_sig()
        count += 1

def ttest():
    a = [2.44,5.55,3.55]
    b  = copy.copy(a)
    print(a)
    for item in range(len(b)):
        b[item] = round(b[item])
    print(a)
    print(b)
    

line = int(input())
if line == 1:
    a = Niro(x,x)
    while True:
        a.nettt()
elif line == 2:
    a = Niro(x,x)
    while True:
        a.nettt_2()
elif line == 3:
    while True:
        brutforce(x,1)
elif line == 4:
    while True:
        brutforce(x,2)

