from sub.a import (
    func_a1,
)  # Absolute import FAIL if run python import_play/b.py (as script), also SUCCESS if run main.py
# from a import func_a1  # SUCCESS if run python sub/b.py, also SUCCESS if run python b.py, FAIL if run main.py, FAIL if run as module mode

# from .a import func_a1 # FAIL if run python sub/b.py, also FAIL if run python b.py, SUCCESS if run main.py


def func_b():
    print("call func_b() in b.py")
    func_a1()
    import sys

    print(sys.path)


if __name__ == "__main__":
    func_b()
