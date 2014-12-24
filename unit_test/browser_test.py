import unittest
from browser.browser import *

class BrowserTest(unittest.TestCase):

    def test_firefox_string(self):
        browser = Browser.factory("Firefox")       
        self.assertEqual(str(browser), "Mozilla Firefox Browser", "Browser is not set to Firefox")          
 
    def test_chrome_string(self):
        browser = Browser.factory("Chrome")
        self.assertEqual(str(browser), "Chrome Browser", "Browser is not set to Chrome")
 
    def test_ie_string(self): 
        browser = Browser.factory("IE")
        self.assertEqual(str(browser), "Windows Internet Explorer Browser", "Browser is not set to IE")
 
    def test_firefox_type(self):
        browser = Browser.factory("Firefox")
        self.assertEqual('Mozilla Firefox', browser.get_name(), "Browser is not set to FireFox")
 
    def test_chrome_type(self):
        browser = Browser.factory("Chrome")
        self.assertEqual('Chrome', browser.get_name(), "Browser is not set to Chrome")
 
    def test_ie_type(self):
        browser = Browser.factory("IE")
        self.assertEqual('Windows Internet Explorer', browser.get_name(), "Browser is not set to IE")
 
    def test_opera_type(self):
        self.assertRaises(InvalidBrowserType, Browser.factory, "Opera")
    