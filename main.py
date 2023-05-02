class Ansi:
    def __init__(self):
        self.save = "\033[s"
        self.load = "\033[u"

    def right(self, num):
        return(f"\033[{num}C")

ANSI = Ansi()

def binput(string: str, var: str):
    string = string.split(var)
    print(ANSI.save)
    out: str = ""
    for text, i in enumerate(string):
        out += str(text)
        if i+1 == len(string):
            break
        if not i:
            current = ""
        current: float = float(input(f"{ANSI.load}{ANSI.right(len(str(1)))}{text}{ANSI.save}"))
        out += str(current)
    print(out)

binput("x = a²", "a")
