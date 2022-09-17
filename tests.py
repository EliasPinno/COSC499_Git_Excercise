import unittest
from unittest.mock import patch
import main

class TestMethods(unittest.TestCase):
    def doInputTest(self, expectedList, inputStr):        
        outputList = main.getListFromInput(inputStr)
        self.assertCountEqual(outputList, expectedList)

    def test_defaultListFromInput(self):
        self.doInputTest([1,2,3,4],"1 2 3 4")

    def test_BigNumbersListFromInput(self):
        self.doInputTest([111111,22,3,854],"111111 22 3 854")

if __name__ == '__main__':
    unittest.main()