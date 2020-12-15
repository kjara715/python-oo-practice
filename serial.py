"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, a):
        "create a serial generator starting from a"
        self.a = a
        self.original_a = a
    def generate(self):
        "increment by 1 from the original value each time this method is run"
        res = self.a
        self.a=self.a+1
        return res #want to return the res then increment it by 1
    
    def reset(self):
        "reset the serial generator back to original value"
        self.a= self.original_a
        


    

