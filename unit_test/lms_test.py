import unittest
from lms.lms import *

class LmsTest(unittest.TestCase):
    
    def test_lms_demo(self):
        
        lms = Lms.factory("D2L-Demo")
        lms.set_user("qarl-admin")
        lms.set_password("Password)9")
        
        self.assertEqual(str(lms), "D2L-Demo", "Lms is not set to D2L-Demo")
        self.assertEqual(lms.get_user(), "qarl-admin", "User Id is not set properly")
        self.assertEqual(lms.get_password(), "Password)9", "Password is not set properly")
        self.assertEqual(lms.get_url(), "https://ryanoggcu.desire2learndemo.com/d2l/login", "Url is not set properly")
        
    def test_lms_test(self):
        
        lms = Lms.factory("D2L-Test")
        lms.set_user("qarl-teacher")
        lms.set_password("Password)9")
        
        self.assertEqual(str(lms), "D2L-Test", "Lms is not set to D2L-Test")
        self.assertEqual(lms.get_user(), "qarl-teacher", "User Id is not set properly")
        self.assertEqual(lms.get_password(), "Password)9", "Password is not set properly")
        self.assertEqual(lms.get_url(), "https://leaptest.desire2learn.com/d2l/login", "Url is not set properly")
        
    def test_lms_knowillage(self):
        
        lms = Lms.factory("D2L-Knowillage")
        lms.set_user("qarl-student1")
        lms.set_password("Password)9")        
        
        self.assertEqual(str(lms), "D2L-Knowillage", "Lms is not set to D2L-Knowillage")
        self.assertEqual(lms.get_user(), "qarl-student1", "User Id is not set properly")
        self.assertEqual(lms.get_password(), "Password)9", "Password is not set properly")                
        self.assertEqual(lms.get_url(), "https://knowillage.desire2learn.com/d2l/login", "Url is not set properly")