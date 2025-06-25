class ball:
    def __init__(self):
        self.pyy()
        self.sym = "a"

    def pyy(self):
        print("world")


class bat(ball):
    def __init__(self):
        super().__init__()
        self.pyy()
        self.sym = "b"


a = [ball(), bat()]


def check(x):
    if x == a[0].sym:
        return "h"
    if x == a[1].sym:
        return "o"


ar = ["    a  b"]
for i, x in enumerate(ar[0]):
    ab = check(x)
    print(ab, i)
