from sikuli import *
from javax.imageio.spi import ImageWriterSpi

project_location = os.path.dirname(getBundlePath())
images_leap = os.path.join(project_location, "images", "leap")
images_browser = os.path.join(project_location, "images", "browser")
images_lms = os.path.join(project_location, "images", "lms")

#addImagePath(images_app)
addImagePath(images_browser)
addImagePath(images_lms)
addImagePath(images_leap)

class Driver(object):
    def __init__(self):
        self.screen = Screen(0)

    def open_lms_in_browser(self,executable, url, name, image): 
        path = executable + " " + url        
        App.open(path)
        
        if self.validate(self.screen, image, 0.50):
            return self.get_browser_window(name)        
        else:
            return None  
        
    def open_browser(self, executable, name, image):
        
        brightspace = "http://www.brightspace.com/"
        
        to_open = executable + " " + brightspace
        
        App.open(to_open)
        
        if self.validate(self.screen, image):
            return self.get_browser_window(name)        
        else:
            return None

    def close_browser(self, name):
        if self.get_browser_window(name):
            App.close(name)

    def goto_lms(self, name, url, image):
        browser_window = self.get_browser_window(name)
        
        if browser_window:
            self.screen.write("#C.l#w1."); self.screen.write("#DEL.#w1."); self.screen.paste(url); self.screen.write("#N.")

        if self.validate(self.screen, image):
            return self.get_browser_window(name)        
        else:
            return None            

    def login(self, name, user, password, image):
        self.screen.write(user)
        self.screen.write("#TAB.")
        self.screen.write(password)
        self.screen.write("#N.")
        
        if self.validate(self.screen, image, 0.50):
            return self.get_browser_window(name)        
        else:
            return None 

    def logout(self, name, user_photo, logout):       
        pattern_for_user = Pattern(user_photo)
        pattern_for_logout = Pattern(logout)
        
        if self.screen.exists(pattern_for_user):
            self.screen.getLastMatch().click()
            
            if self.screen.exists(pattern_for_logout):
                self.screen.getLastMatch().click()
        else:
            print "Either image " + user_photo + " or " + logout + " was not found."      

    def open_course(self, name, course_name, search_for_courses, content):
        pattern_for_search = Pattern(search_for_courses).similar(0.50)
        #pattern_for_content = Pattern(content)
        
        if self.screen.exists(pattern_for_search):
            self.screen.getLastMatch().click()
            self.screen.getLastMatch().write(course_name)
            self.screen.getLastMatch().write("#N.")
            
            if self.validate(self.screen, content, 0.80):
                if self.screen.exists(content):
                    self.screen.getLastMatch().click()
        else:
            print "Either image " + search_for_courses + " or " + content + " was not found."   

    def add_leap_activity(self, name, new_leap_name, add_activities, remote_plugin):
        pattern_for_activities = Pattern(add_activities)
        pattern_for_remote = Pattern(remote_plugin)
        
        if self.screen.exists(pattern_for_activities):
            self.screen.getLastMatch().click()
            
            if self.screen.exists(pattern_for_remote):
                self.screen.getLastMatch().click()
                                      
    def get_browser_window(self, name):
        browser = App(name)
        browser_window = None
        for i in range(3):
            if browser.window(0) == None:
                self.screen.wait(1)
                continue
            for i in range(100):
                browser_window = browser.window(i)
                if browser_window == None:
                    break
                if browser_window.w < 350:
                    continue
                break
            break
        return browser_window

    def validate(self, screen, image, similar=0.75, time_out=10):
        #screen.focus()
        screen.highlight(2)
        
        pattern = Pattern(image).similar(similar)
        for counter in range(1,time_out):
            if not screen.exists(pattern):
                screen.wait(1)
            else:
                screen.getLastMatch().highlight(2)
                print "Image: " + image + " was found after " + str(counter) + " tries"
                return True
        
        print "Image: " + image + " was not found after " + str(time_out) + " tries"
        
        return False                        