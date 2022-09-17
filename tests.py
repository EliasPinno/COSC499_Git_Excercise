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

    def test_LSortedStandard(self):
        self.assertCountEqual(main.sortList([287,45,360,20]),[20,45,287,360])

    def test_LSortedRepeats(self):
        self.assertCountEqual(main.sortList([45,45,10,45]),[10,45,45,45])

    def test_LSortedReverseStandard(self):
        self.assertCountEqual(main.sortList([287,45,360,20]),[360,287,45,20])
        
    def test_LSortedReverseRepeats(self):
        self.assertCountEqual(main.sortList([45,45,10,45]),[45,45,45,10])

if __name__ == '__main__':
    unittest.main()