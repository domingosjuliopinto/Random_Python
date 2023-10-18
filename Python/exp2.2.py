# program to demonstrate exception handling in python
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is <0"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


a = int(input("Enter a:"))    
b = int(input("Enter b:"))    
try:
    if a < 0 or b < 0:
            raise ValueTooSmallError
    if a > 100 or b > 100:
            raise ValueTooLargeError
    print(a/b)
    print('10'+10)
except TypeError:
          print("'10' + 10, You added values of incompatible types, so it won't be printed")
except ZeroDivisionError:
          print("You divided by 0")
except ValueTooSmallError:
        print("This value is too small")
except ValueTooLargeError:
        print("This value is too large")
