class Borg():
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Debug(Borg):
    def __init__(self, arg=None):
        if arg is not None:
            self.isDebugging = arg
        
    def __str__(self):
        return self.isDebugging

    def __boolean__(self):
        return self.isDebugging
    
