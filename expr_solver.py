"""
Expression solver class.
"""

import math
from ansi import Ansi

class Solver:
    """
    Expression solver class.
    """
    def __init__(self):
        self.ansi = Ansi()

    def get_vars(self, expr, split_char, out_type=int):
        """From an input expression returns a list with numbers inputed by the user"""
        split_expr = expr.split(split_char) # ['0 = ', 'x² + ', 'x + ', '']

        out = []
        for idx, split_str in enumerate(split_expr):
            if not idx:
                inp_str = split_str + self.ansi.save
                out.append(input(inp_str))
            elif idx == len(split_expr) - 1:
                print(self.ansi.load + self.ansi.move_right(len(out[idx - 1])) + split_str)
            else:
                inp_str = self.ansi.load + self.ansi.move_right(len(out[idx - 1])) + split_str \
                    + self.ansi.save
                out.append(input(inp_str))

        try:
            out = [out_type(x) for x in out]
        except ValueError:
            out_type = str(out_type)[8:-2]
            print(f"Some value is not a{'n' if out_type == int else ''} {out_type}, the inputs are invalid.")
            out = False

        return out

    def quadratic(self, a_var, b_var, c_var, return_delta = False):
        """
        Returns a list with x' and x", only returns delta if needed
        Full formula => -b+-sqrt(b²-4ac)/2a
        """
        delta = b_var**2-4*a_var*c_var
        if delta < 0:
            return None

        x1_var = (-b_var+math.sqrt(delta))/2*a_var
        x2_var = (-b_var-math.sqrt(delta))/2*a_var
        out = [x1_var, x2_var]
        if return_delta:
            out.append(delta)
        return out

    def pythagorean(self, a_var, b_var):
        """
        Returns c
        Full formula => a² + b² = c²  ==  c = √a² + b²
        """
        return math.sqrt(a_var**2 + b_var**2)
