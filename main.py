"""
Currently only has a quadratic equation solver, i'll add some physics formulas later
"""

import os
from expr_solver import Solver

def main():
    """Main entry point"""
    solver = Solver()

    while True:
        os.system("clear")
        print("    Types                Alias         Expression      Variable to Find")
        print(" - Quadratic Equation   (q)       =>  ax² + bx + c = 0  =>  x', x\"")
        print(" - Pythagorean theorem  (p / pc)  =>  a² + b² = c²      =>  c")
        # print(" -          ||          (pa)      =>  a = √c² - b²      =>  a")
        # print(" -          ||          (pb)      =>  b = √c² - a²      =>  b")
        expr_type = input("What is the expression? (Type anything else to exit) ").lower()
        os.system("clear")

        match expr_type:
            case "q":
                print("Quadratic equation solver (ax² + bx + c = 0)")
                print("Type each float in order (a, b, c)")
                abc = solver.get_vars("nx² + nx + n = 0", "n", float)
                if abc:
                    ans = solver.quadratic(abc[0], abc[1], abc[2], True)
                    if not ans:
                        print("Delta is negative, the inputs are invalid.")
                    else:
                        print(f"delta = {ans[2]}, x' = {ans[0]}, x\" = {ans[1]}")
            case "p"|"pc":
                print("Pythagorean theorem solver (a² + b² = c²)")
                print("Type each float in order (a, b)")
                ab_vars = solver.get_vars("n² + n² = c²", "n", float)
                if ab_vars:
                    ans = solver.pythagorean(ab_vars[0], ab_vars[1])
                    print(f"c = {ans}")
            case _:
                break

        print("\nContinue? (y/n)")
        if input("> ").lower() != "y":
            break

# Quadratic Test cases

# a = 1, b = 3, c = -4
# delta = 25, x' = 1, x" = -4

# a = 1, b = -3, c = -10
# delta = 49, x' = 5, x" = -2

# a = 6, b = -17, c = 12
# delta = 1, x' = 54, x" = 48

if __name__ == "__main__":
    main()
