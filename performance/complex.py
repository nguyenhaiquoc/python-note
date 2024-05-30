# python -m cProfile complex.py
# pyinstrument -o pyinstrument.html -r html complex.py
# py-spy record -o profile.svg --pid $PID  # attach py-spy to the running process, suitable for production
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def complex_function():
    # CPU task
    for i in range(1000):
        fibonacci(20)

    # I/O task
    with open("output.txt", "w") as file:
        file.write("This is some output.")

    # Simulate some more CPU work
    time.sleep(2)

    # I/O task
    with open("input.txt", "r") as file:
        data = file.read()

    return data


if __name__ == "__main__":
    complex_function()
