from sub.subsub.c import func_c
from sub.b import func_b


if __name__ == "__main__":
    import sys

    print(sys.path)
    print("Hello World!")
    func_b()
    func_c()
