"""This is the module that will start the app."""
import gui
import argparse
import message_ops as MO


if __name__ == '__main__':
    # Input Flags to determine interface type and path to input file.
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface', type=str, default="cli")
    parser.add_argument('--path', type=str, default="input")
    args = parser.parse_args()

    # Starts the desired interface.
    if args.interface == "gui":
        gui.GuiApplication().run("Message Generation", "950x1000")
    else:
        if args.path == "input":
            print(MO.manualInput(input(r"Please input your messages with the delimiter '\n': ").replace(r'\n', '\n')))
        else:
            print(MO.fileImport(args.path))