import abc

class Lms(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, lms_name):
        self.lms_name = lms_name
        self.user = None
        self.password = None
        self.url = "Provide your own url"
        self.validation_image = "login.png"
        self.select_course = "select_course.png"
        self.last_10_courses = "last_10_courses.png"
        self.search_for_courses = "search_for_courses.png"
        self.user_photo = "user_photo.png"
        self.logout = "log_out.png"
        self.content = "content.png"
        self.add_activities = "add_activities.png"
        
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
    
    def get_select_course(self):
        return self.select_course    
    
    def get_last_10_courses(self):
        return self.last_10_courses       

    def get_search_for_courses(self):
        return self.search_for_courses    

    def get_user_photo(self):
        return self.user_photo
    
    def get_logout(self):
        return self.logout  
    
    def get_content(self):
        return self.content      
    
    def get_add_activities(self):
        return self.add_activities     
                    
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


        
        