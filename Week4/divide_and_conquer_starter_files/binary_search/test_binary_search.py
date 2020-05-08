import unittest
import binary_search

testArray=[]
with open('testdata', 'r') as f:
    for line in f:
        testArray.append(int(line.strip('\n')))

class TestBinarySearch(unittest.TestCase):
    def test_linear_search(self):
        #testArray = [1, 2, 3, 120, 1000, 9999]
        print(testArray)
        self.assertEqual(binary_search.binary_search(testArray, 41), 9)
        self.assertEqual(binary_search.binary_search(testArray, 20), 100)
        self.assertEqual(binary_search.binary_search(testArray, 1000), -1)


if __name__ == '__main__':
    unittest.main()
