from driver.driver import *

class Workflow(object):
    
    def __init__(self, browser, lms):
        self.browser = browser
        self.lms = lms
        self.driver = Driver()
        
    def open_browser(self):
        self.driver.open_browser(self.browser.get_executable(), self.browser.get_name(), self.browser.get_validation_image())
        
    def close_browser(self):
        self.driver.close_browser(self.browser.get_name())
        
    def goto_lms(self):
        self.driver.goto_lms(self.browser.get_name(), self.lms.get_url(), self.lms.get_validation_image())
        
    def login(self):
        self.driver.login(self.browser.get_name(), self.lms.get_user(), self.lms.get_password(), self.lms.get_select_course())    
        
    