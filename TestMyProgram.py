import unittest
import requests
import scrapytest

url = "http://172.18.58.80/hr2"


# Each test class must be a subclass of unittest.TestCase
# The class should be named as TestXXXX to indicate to the program that it is a test program
class TestMyProgram(unittest.TestCase):

    # All methods should be named as test_XXXX to indicate that it is a test case
    def test_upper(self):
        self.assertEqual(scrapytest.NewSpider.start_urls == 'http://172.18.58.80/hr2')

    def test_isupper(self):
        self.assertTrue('HTTP://172.18.58.80/HR2'.isupper())
        self.assertFalse('http://172.18.58.80/hr2'.isupper())
    # Checking whether the url is responding to requests
    def test_TestUrl(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print("[TestUrl] URL OK")
            else:
                print("[TestUrl] Requested URL not found")
        except Exception as e:
            print("[TestUrl] Error: ", {e})

    def test_TestCase_2(self):
        print("[TestCase_2] Test case 2")


# Must invoke the unittest.main() methods
if __name__ == '__main__':
    unittest.main()
