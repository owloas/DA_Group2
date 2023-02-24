import unittest
from scrapytest import NewSpider

class TestNewSpider(unittest.TestCase):
    def test_start_urls(self):
        spider = NewSpider()
        self.assertEqual(spider.start_urls[0], 'http://172.18.58.80/hr2', "Start URL is not http://172.18.58.80/hr2")