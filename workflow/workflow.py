from driver.driver import *
from lms.lms import *
from browser.browser import *
from leap.leap import *

class Workflow(object):
    
    def __init__(self, browser_name, lms_name, leap_deployment):
        self.browser = Browser.factory(browser_name)
        self.lms = Lms.factory(lms_name)
        self.leap_deployment = Leap.factory(leap_deployment)
        self.driver = Driver()
        
    def open_browser(self):
        self.driver.open_browser(self.browser.get_executable(), self.browser.get_name(), self.browser.get_validation_image())
        
    def close_browser(self):
        self.driver.close_browser(self.browser.get_name())
        
    def goto_lms(self):
        self.driver.goto_lms(self.browser.get_name(), self.lms.get_url(), self.lms.get_validation_image())
        
    def login(self, user, password):
        self.driver.login(self.browser.get_name(), user, password, self.lms.get_search_for_courses())    
        
    def open_lms_in_browser(self):
        self.driver.open_lms_in_browser(self.browser.get_executable(), self.lms.get_url(), self.browser.get_name(), self.lms.get_validation_image())
        
    def logout(self):
        self.driver.logout(self.browser.get_name(), self.lms.get_user_photo(), self.lms.get_logout())
        
    def open_course(self, course_name):
        self.driver.open_course(self.browser.get_name(), course_name, self.lms.get_search_for_courses(), self.lms.get_content())
        
    def add_leap_activity(self, new_leap_name):
        self.driver.add_leap_activity(self.browser.get_name(), new_leap_name, self.lms.get_add_activities(), self.leap_deployment.get_remote_plugin())
        