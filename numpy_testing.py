

import numpy as np
import time


def main():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print('shape: {}'.format(a.shape))
    print('number of dimensions: {}'.format(a.ndim))
    print('data type: {}'.format(a.dtype.name))
    print('item size: {}'.format(a.itemsize))
    print('size: {}'.format(a.size))
    print('type: {}'.format(type(a)))

    b = np.array([(1, 2, 3), (9, 8, 7)]) # list of sequences
    print('b: {}'.format(b))

    complex_array = np.array([(1.0, 2.0), (3.5, 4.6)], dtype='complex')
    print('Complex array: {}'.format(complex_array))

    print('ZEROS: {}'.format(np.zeros((2, 8))))
    print('ONES: {}'.format(np.ones((3, 5))))
    print('EMPTY: {}'.format(np.empty((4, 4))))

    print(np.arange(12).reshape(4, 3))

    b = np.array([50, 60, 70, 80])
    a = np.arange((b.shape[0]))

    t1 = time.perf_counter()
    c = b - a
    t2 = time.perf_counter()
    print('Time for element-wise subtraction: {}'.format(t2 - t1))
    print(np.sin(c))

    y = np.array([[1, 1], [2, 7]])
    z = np.array([[2, 3], [1, 1]])
    print('Element-wise product: {}'.format(y * z))
    print('Matrix product: {}'.format(y @ z))
    print('Reverse matrix product: {}'.format(z @ y))
    print('Different matrix product: {}'.format(y.dot(z)))


if __name__ == '__main__':
    main()


