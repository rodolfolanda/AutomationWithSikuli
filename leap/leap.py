import abc

class Leap(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, leap_deployment):
        self.leap_deployment = leap_deployment
        self.remote_plugin = "Provide your own remote plugin name"
        
    def __str__(self):
        return self.leap_deployment  
    
    def factory(leap_deployment):
        if leap_deployment == "LeaP QA":
            return LeapQA("LeaP QA")
        
        if leap_deployment == "LeaP Dev":
            return  LeapDev("LeaP Dev")
        
        if leap_deployment == "LeaP Cert":
            return LeapCert("LeaP Cert")

        raise InvalidLeapType("Bad leap Deployment creation: " + leap_deployment)

    factory = staticmethod(factory)    
    
    def get_remote_plugin(self):
        return self.remote_plugin

class LeapQA(Leap):
    def __init__(self, leap_deployment):
        Leap.__init__(self, leap_deployment)
        self.remote_plugin = "Auto QA.png"
        
class LeapDev(Leap):
    def __init__(self, leap_deployment):
        Leap.__init__(self, leap_deployment)
        self.remote_plugin = "D2L LeaP (leapdev)"

class LeapCert(Leap):
    def __init__(self, leap_deployment):
        Leap.__init__(self, leap_deployment)
        self.remote_plugin = "D2L LeaP (Cert)"
                    
class LeapError(Exception): pass
class InvalidLeapType(LeapError): pass        
        