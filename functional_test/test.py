import unittest
from lms.lms import *
from browser.browser import *
from workflow.workflow import *

class FunctionalTest(unittest.TestCase):
    
#     def __init__(self, testname, browser):
#         #unittest.TestCase.__init__(self, testname)
#         super(FunctionalTest, self).__init__(self, testname)
#         self.browser = browser
    
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
         
    def wizard_workflow(self, name, full_name):
         
        #Setting up the Browser to be used
        browser = Browser.factory(name)
         
        self.assertEqual(full_name, browser.get_name(), "Browser is not set to " + name)
         
        # Setting up the LMS that is going to be tested: url and userid / password
        lms = Lms.factory("D2L-Demo")
         
        lms.set_user("qarl-admin")
        lms.set_password("Password)9")
         
        self.assertEqual(lms.get_url(), "https://ryanoggcu.desire2learndemo.com/d2l/login", "Url is not set properly")
                     
        # Work-flow starts by opening a specific browser
        flow = Workflow(browser, lms)
         
        flow.open_browser()
         
        flow.goto_lms()
        
        flow.login()
         
        flow.close_browser()
        
#     def test_wizard_with_ie(self):
#         self.wizard_workflow("IE", "Windows Internet Explorer")
#             
#     def test_wizard_with_chrome(self):
#         self.wizard_workflow("Chrome", "Chrome")

    def test_wizard_with_firefox(self):
        self.wizard_workflow("Firefox", "Mozilla Firefox")
                        
if __name__ == '__main__':
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FunctionalTest("test_wizard_with_ie"))
    suite.addTest(FunctionalTest("test_wizard_with_chrome"))
    suite.addTest(FunctionalTest("test_wizard_with_firefox"))
    unittest.TextTestRunner(verbosity=2).run(suite)
    
                     
        