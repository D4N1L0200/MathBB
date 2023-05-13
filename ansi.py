"""
Class to move the console cursor
"""

class Ansi:
    """
    Class to move the console cursor
    """
    def __init__(self):
        self.save = "\033[s"
        self.load = "\033[u"

    def move_up(self, num = 1):
        """Moves the console cursor 1 character upwards"""
        return f"\033[{num}A"

    def move_down(self, num = 1):
        """Moves the console cursor 1 character downwards"""
        return f"\033[{num}B"

    def move_right(self, num = 1):
        """Moves the console cursor 1 character right"""
        return f"\033[{num}C"

    def move_left(self, num = 1):
        """Moves the console cursor 1 character left"""
        return f"\033[{num}D"
