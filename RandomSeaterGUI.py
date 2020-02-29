"""
Serves as an entry point for building the GUI application
"""
from main import main


class GUIArgs():
    def __init__(self):
        self.use_gui = True


if __name__ == '__main__':
    args = GUIArgs()
    main(args)
