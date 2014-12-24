import abc

class Lms(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, lms_name):
        self.lms_name = lms_name
        self.user = None
        self.password = None
        self.url = "Provide your own url"
        self.validation_image = "college_banner.png"
        
    def __str__(self):
        return self.lms_name        
    
    def factory(lms_name):
        if lms_name == "D2L-Demo":
            return D2lDemo("D2L-Demo")
        
        if lms_name == "D2L-Test":
            return  D2lTest("D2L-Test")
        
        if lms_name == "D2L-Knowillage":
            return D2lKnowillage("D2L-Knowillage")

        raise InvalidLmsType("Bad lms creation: " + lms_name)

    factory = staticmethod(factory)
    
    def set_user(self, user):
        self.user = user
        
    def set_password(self, password):
        self.password = password
        
    def get_user(self):
        return self.user
    
    def get_password(self):
        return self.password
    
    def get_url(self):
        return self.url
    
    def get_validation_image(self):
        return self.validation_image    
    
class D2lDemo(Lms):
    def __init__(self, lms_name):
        Lms.__init__(self, lms_name)
        self.url = "https://ryanoggcu.desire2learndemo.com/d2l/login"
        

class D2lTest(Lms):
    def __init__(self, lms_name):
        Lms.__init__(self, lms_name)
        self.url = "https://leaptest.desire2learn.com/d2l/login"
        
class D2lKnowillage(Lms):
    def __init__(self, lms_name):
        Lms.__init__(self, lms_name)
        self.url = "https://knowillage.desire2learn.com/d2l/login"
        

class LmsError(Exception): pass
class InvalidLmsType(LmsError): pass


        
        