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
    def __init__(self, start=0):
        '''creating new generator stating at 0'''
        self.start = self.next = start 
        def __repr__(self):
            '''show string representation'''
            return f'<SerialGenerator start={self.start} next={self.next}>'
        def generate(self):
            '''return the current value and update it for future calls.'''
            self.next += 1
            result = self.current -1
        def reset (self):
            '''set back to starting point'''
            self.next = self.start

