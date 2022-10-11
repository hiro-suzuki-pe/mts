import unittest
import numpy as np
import mts

class Test_Mspace(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init＿NoParm(self):
        m_s = mts.m_space()
        self.assertEqual([], m_s.data_list)

class TestMts(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_orthogonal_array(self):
        expected = np.array([[1,1,1],[1,2,2],[2,1,2],[2,2,1]])
        mt = mts.mts([])
        self.assertEqual(expected.all(), mt.orthogonal_array(3).all())

#    def test_list(self):
#
#         self.assertEqual([1, 2, [3, 4]], [1,2,  [3, 4]])

if __name__ == '__main__':
    unittest.main()
