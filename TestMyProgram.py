import unittest
import requests
from scrapytest import NewSpider

#To check if url in scrapytest.py is the correct url
class TestNewSpider(unittest.TestCase):
    def test_start_urls(self):
        spider = NewSpider()
        self.assertEqual(spider.start_urls[0], 'http://172.18.58.80/hr2', "Start URL is not http://172.18.58.80/hr2")

url = "http://172.18.58.80/hr2"

class TestMyProgram(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
