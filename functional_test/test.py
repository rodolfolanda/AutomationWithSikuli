import unittest
from lms.lms import *
from browser.browser import *
from workflow.workflow import *

class FunctionalTest(unittest.TestCase):
    
#     def __init__(self, testname, browser):
#         #unittest.TestCase.__init__(self, testname)
#         super(FunctionalTest, self).__init__(self, testname)
#         self.browser = browser
             
    def wizard_workflow(self, browser_name, lms_name, leap_deployment):
                            
        # Work-flow starts by opening a specific browser
        flow = Workflow(browser_name, lms_name, leap_deployment)
               
        flow.open_lms_in_browser()
        
        flow.login("qarl-admin", "Password)9")
        
        flow.open_course("LeaP QA Automation")
        
        flow.add_leap_activity("LeaP QA 01")
                
        flow.logout()
                 
        flow.close_browser()
        
    def test_wizard_with_ie(self):
        self.wizard_workflow("IE", "D2L-Demo", "LeaP QA")
             
#     def test_wizard_with_chrome(self):
#         self.wizard_workflow("Chrome", "D2L-Demo", "LeaP QA")
     
#     def test_wizard_with_firefox(self):
#         self.wizard_workflow("Firefox", "D2L-Demo", "LeaP QA")
                        
if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FunctionalTest("test_wizard_with_ie"))
    #suite.addTest(FunctionalTest("test_wizard_with_chrome"))
    #suite.addTest(FunctionalTest("test_wizard_with_firefox"))
    unittest.TextTestRunner(verbosity=2).run(suite)
    
                     
        