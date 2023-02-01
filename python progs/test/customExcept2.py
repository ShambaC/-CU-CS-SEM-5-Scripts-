class CustExc(Exception) :
    pass

try :
    raise CustExc
except CustExc :
    print("Custom exception occured")