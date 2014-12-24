import unittest
from lms.lms import *
from browser.browser import *
from workflow.workflow import *

class FunctionalTest(unittest.TestCase):
    
#     def test_wizard_workflow_chrome(self):
#         
#         #Setting up the Browser to be used
#         browser = Browser.factory("Chrome")
#         
#         self.assertEqual('Chrome', browser.get_name(), "Browser is not set to Chrome")
#         
#         # Setting up the LMS that is going to be tested: url and userid / password
#         lms = Lms.factory("D2L-Demo")
#         
#         lms.set_user("qarl-admin")
#         lms.set_password("Password)9")
#         
#         self.assertEqual(lms.get_url(), "https://ryanoggcu.desire2learndemo.com/d2l/login", "Url is not set properly")
#                     
#         # Work-flow starts by opening a specific browser
#         flow = Workflow(browser, lms)
#         
#         flow.open_browser()
#         
#         flow.goto_lms()
#         
#         flow.close_browser()
        
#     def test_wizard_workflow_firefox(self):
#          
#         #Setting up the Browser to be used
#         browser = Browser.factory("Firefox")
#          
#         self.assertEqual('Mozilla Firefox', browser.get_name(), "Browser is not set to Firefox")
#          
#         # Setting up the LMS that is going to be tested: url and userid / password
#         lms = Lms.factory("D2L-Demo")
#          
#         lms.set_user("qarl-admin")
#         lms.set_password("Password)9")
#          
#         self.assertEqual(lms.get_url(), "https://ryanoggcu.desire2learndemo.com/d2l/login", "Url is not set properly")
#                      
#         # Work-flow starts by opening a specific browser
#         flow = Workflow(browser, lms)
#          
#         flow.open_browser()
#          
#         flow.goto_lms()
#          
#         flow.close_browser()        
         
    def test_wizard_workflow_ie(self):
         
        #Setting up the Browser to be used
        browser = Browser.factory("IE")
         
        self.assertEqual('Windows Internet Explorer', browser.get_name(), "Browser is not set to IE")
         
        # Setting up the LMS that is going to be tested: url and userid / password
        lms = Lms.factory("D2L-Demo")
         
        lms.set_user("qarl-admin")
        lms.set_password("Password)9")
         
        self.assertEqual(lms.get_url(), "https://ryanoggcu.desire2learndemo.com/d2l/login", "Url is not set properly")
                     
        # Work-flow starts by opening a specific browser
        flow = Workflow(browser, lms)
         
        flow.open_browser()
         
        flow.goto_lms()
         
        flow.close_browser()         
        