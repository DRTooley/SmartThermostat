class Debug():
    __instance = None
    def __new__(cls, arg=None):
        if Debug.__instance is None:
            Debug.__instance = object.__new__(cls)

        if arg is not None:
            Debug.__instance.isDebugging = arg

        return Debug.__instance

    def GetInfo(cls):
        return Debug.__instance.isDebugging
