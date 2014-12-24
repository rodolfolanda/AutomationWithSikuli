from sikuli import *

project_location = os.path.dirname(getBundlePath())
#images_app = os.path.join(project_location, "images", "app")
images_browser = os.path.join(project_location, "images", "browser")
images_lms = os.path.join(project_location, "images", "lms")

#addImagePath(images_app)
addImagePath(images_browser)
addImagePath(images_lms)

class Driver(object):
    def __init__(self):
        self.screen = Screen(0)
        
    def open_browser(self, executable, name, image):
        App.open(executable)
        
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

    def validate(self, screen, image, time_out=10):
        for counter in range(1,time_out):
            if not screen.exists(image):
                screen.wait(1)
            else:
                screen.getLastMatch().highlight(2)
                print "Image: " + image + " was found after " + str(counter) + " tries"
                return True
        
        print "Image: " + image + " was not found after " + str(time_out) + " tries"
        
        return False                        