import platform


def hello():
    print("Helo world!")
    print("Platform: {}".format(platform.platform()))
    print("Compiler: {}".format(platform.python_compiler()))
    print("Python: {}".format(platform.python_version()))


if __name__ == "__main__":
    hello()
