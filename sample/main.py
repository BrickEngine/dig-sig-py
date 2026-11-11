# 1. Matrix erstellen
# 2. linear space erstellen (linspace): Startwert, Endwert, Anzahl -> Array
# 3. Meshgrid (x_vec, y_vec) -> x_mat, y_mat
# 4. Mandelbrot for each pixel in x_mat, y_mat
# 5. Mandelbrot plot

import numpy as np
import matplotlib.pyplot as plt

from mandelbrot import mandelbrot, mandelbrot_vec

x_start = -2
x_end = 1

y_start = -1
y_end = 1

x_pixel = 500 * 2
y_pixel = np.int(x_pixel * (y_end - y_start) / (x_end - x_start))

x_vec = np.linspace(x_start, x_end, x_pixel)
y_vec = np.linspace(y_start, y_end, y_pixel)

# x_mat, y_mat = np.meshgrid(x_vec, y_vec, indexing='ij')

maxiter = 100 * 2

# x_flat = x_mat.ravel()
# y_flat = y_mat.ravel()

# mat = mandelbrot(x_flat, y_flat, maxiter)
# mat = np.transpose(mat.reshape((x_pixel, y_pixel)))
mat = mandelbrot_vec(x_vec, y_vec, maxiter)
mat = np.transpose(mat)

plt.imshow(mat)
plt.show()