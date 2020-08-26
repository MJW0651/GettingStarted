import unittest
from main_source import helloWorld

class MyTestCase(unittest.TestCase):
    def testHelloMessage(self):
        self.assertEqual("Hello, CIS 189! ", helloWorld.helloMessage())


if __name__ == '__main__':
    unittest.main()
