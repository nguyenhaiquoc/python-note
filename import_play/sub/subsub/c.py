# from sub.b import func_b  # work
from ..b import func_b  # also work


def func_c():
    print("call func_c() in c.py")
    func_b()


if __name__ == "__main__":
    func_c()
