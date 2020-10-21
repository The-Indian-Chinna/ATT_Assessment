"""This is the module that will start the app."""
import gui
import argparse
import message_ops as MO


if __name__ == '__main__':
    # Input Flags to determine interface type and path to input file.
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface', type=str, default="cli")
    parser.add_argument('--window_size', type=str, default="950x1000")
    parser.add_argument('--path', type=str, default="input")
    args = parser.parse_args()

    # Starts the desired interface.
    if args.interface.strip().lower() == "gui":
        window_size = args.window_size.strip().lower().split("x")
        if len(window_size) == 2 and window_size[0].isnumeric() and window_size[1].isnumeric():
            gui.GuiApplication("Message Generation", [int(x) for x in window_size]).run()
        else:
            raise Exception("Incorrect Window Size Format, must fit the format WidthxHeight. EX:950x1000")
    else:
        if args.path.strip().lower() == "input":
            print(MO.manualInput(input(r"Please input your messages with the delimiter '\n': ").replace(r'\n', '\n')))
        else:
            print(MO.fileImport(args.path))