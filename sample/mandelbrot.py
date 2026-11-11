import numpy as np

def mandelbrot(x, y, maxiter = 100):
    
    mat = np.zeros(x.size)

    for i in range(x.size):
        print(i, x.size)
        c = complex(x[i], y[i])
        z = complex(0, 0)

        for n in range(maxiter):
            z = z * z + c
            if z.real * z.real + z.imag * z.imag > 4.0:
                mat[i] = n + 1 - np.log(np.log(np.abs(z * z + c))) / np.log(2)
                break
        
    return mat

def mandelbrot_vec(x, y, maxiter = 100):
    
    mat = np.zeros((x.size, y.size))

    for i in range(x.size):
        print(i+1, x.size)
        for j in range(y.size):
            c = complex(x[i], y[j])
            z = complex(0, 0)

            for n in range(maxiter):
                z = z * z + c
                if z.real * z.real + z.imag * z.imag > 4.0:
                    # mat[i, j] = n + 1 - np.log(np.log(np.abs(z * z + c))) / np.log(2)
                    mat[i, j] = n + 1
                    break
            
            # n = 0
            # while (np.abs(z) < 2.0) and (n < maxiter):
            #     z = z * z + c

        
    return mat