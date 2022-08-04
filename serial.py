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
        self.start = start
        self.serial = start

    def __repr__(self):
        """Display representation"""

        return f"SerialGenerator start={self.start} serial={self.serial}"

    def generate(self):
        """Generate the next serial number"""
        self.serial += 1
        return self.serial - 1

    def reset(self):
        """Reset the serial number to the start number"""
        self.serial = self.start
