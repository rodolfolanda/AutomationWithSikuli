import abc

class Browser(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.path_to_executable = "Provide your own path"
        self.validation_image = "brightspace.png"
        
    def __str__(self):
        return str(self.browser_name) + " Browser"
    
    def get_name(self):
        return self.browser_name

    def get_executable(self):
        return self.path_to_executable
    
    def get_validation_image(self):
        return self.validation_image
    
    def factory(browser_name):
        if browser_name == "Firefox":
            return Firefox("Mozilla Firefox")
        
        if browser_name == "Chrome":
            return  Chrome("Chrome")
        
        if browser_name == "IE":
            return IE("Windows Internet Explorer")

        raise InvalidBrowserType("Bad browser creation: " + browser_name)

    factory = staticmethod(factory)
    

class Firefox(Browser):
    
    def __init__(self, browser_name):
        Browser.__init__(self, browser_name)
        self.path_to_executable = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        #self.validation_image = "brightspace.png"
        #self.login_image = "login.png"
        
class Chrome(Browser):
    
    def __init__(self, browser_name):
        Browser.__init__(self, browser_name)
        self.path_to_executable = r"C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
        #self.validation_image = "brightspace.png"
        #self.login_image = "login.png"
        
class IE(Browser):

    def __init__(self, browser_name):
        Browser.__init__(self, browser_name)
        self.path_to_executable = "C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe"
        #self.validation_image = "brightspace.png"
        #self.login_image = "login.png"

class BrowserError(Exception): pass
class InvalidBrowserType(BrowserError): pass        
                        
                