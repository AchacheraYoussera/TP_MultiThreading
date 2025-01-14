import unittest
import numpy as np
import numpy.testing as npt
import task

class TestMatrixMultiplication(unittest.TestCase):

    def test_matrix_multiplication(self):
        T=task()
        A = T.a
        x = T.x           
        B = T.b       
        result = np.dot(A, x)
        npt.assert_allclose(result, B, rtol=1e-5, atol=1e-8, err_msg="A * x n'est pas égal à B")

if __name__ == '__main__':
    unittest.main()
