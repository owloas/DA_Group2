import unittest

class TestMyProgram(unittest.TestCase):

    def test_web(self):
        self.assertEqual('http://172.18.58.80/hr2'.upper(), 'HTTP://172.18.58.80/HR2')

    def test_isupper(self):
        self.assertTrue('HTTP://172.18.58.80/HR2'.isupper())
        self.assertFalse('http://172.18.58.80/hr2'.isupper())

if __name__ == '__main__':
    unittest.main()