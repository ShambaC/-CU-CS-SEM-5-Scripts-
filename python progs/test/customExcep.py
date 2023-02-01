class NiggaExecpt(Exception) :
    def __init__(self, msg="Default custom") :
        self.message = msg
        super().__init__(self.message)    


# raise NiggaExecpt("Nigga excepted")

try :
    print("Hello")
    raise NiggaExecpt
except NiggaExecpt :
    print("Nigga excpeted")
finally :
    print('Finally !!')