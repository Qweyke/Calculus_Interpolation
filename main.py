""" Интерполяция многочленами Лагранжа на равномерной и Чебышевской сетке

Бояршинов МГ, 2006 -- Численные методы.ч4
"""


import math
import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return abs(x)


def chebishev(i, a, b, n):
    res = ((b + a) / 2) + ((b - a) / 2) * math.cos(((2 * i + 1) * math.pi) / (2 * n))
    return res


def basic_polynomial(x, x_i,  xj_values):  # высчитать значение базового полинома для искомой точки в узле x_i
    poly = 1
    for j in range(len(xj_values)):
        if x_i != xj_values[j]:
            poly *= (x - xj_values[j]) / (x_i - xj_values[j])
    return poly


def lagrange_polynomial(x, xi_values, yi_values):  # высчитывает
    y = 0
    for i in range(len(xi_values)):
        y += yi_values[i] * basic_polynomial(x, xi_values[i], xi_values)
    return y


x_values = [-1, -0.5, 0, 0.5, 1]
y_values = [func(x) for x in x_values]

x_values_interp = np.linspace(-1, 1, 100)
x_values_chebishev = [chebishev(i, 1, -1, 100) for i in range(100)]

y_values_interp = []
y_values_chebishev = []

i = 0
for x in x_values_interp:
    y_values_interp.append(lagrange_polynomial(x, x_values, y_values))
    print("(обычный x), y = ", lagrange_polynomial(x, x_values, y_values))
    y_values_chebishev.append(lagrange_polynomial(chebishev(i, 1, -1, 100), x_values, y_values))
    print("(чебышевский x), y = ", lagrange_polynomial(chebishev(i, 1, -1, 100), x_values, y_values))
    i += 1

plt.plot(x_values, y_values, color='green', label='Изначальная функция')
plt.plot(x_values_interp, y_values_interp, color='blue', label='Интерполированная функция')
plt.plot(x_values_chebishev, y_values_chebishev, color='red', ls='--', label='Интерполированная функция на'
                                                                             ' чебышевской сетке')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
