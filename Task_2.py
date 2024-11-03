import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2 

# Метод Монте-Карло
def monte_carlo_integration(func, a, b, num_points=100000):
    x_random = np.random.uniform(a, b, num_points)
    y_random = func(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

mc_result = monte_carlo_integration(f, a, b)
print("Інтеграл (Метод Монте-Карло):", mc_result)

quad_result, quad_error = spi.quad(f, a, b)
print("Інтеграл (Функція quad):", quad_result)
print("Похибка:", quad_error)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b, 100)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()
