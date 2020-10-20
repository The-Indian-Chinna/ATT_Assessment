"""This module handles the gui elements for the oldest common animal string generation"""
import tkinter as tk
from tkinter import filedialog
import message_ops as MO
import sys

class GuiApplication:
    """This is the gui that the user interacts with to generate the oldest common animal string"""
    def __init__(self):
        """Intializes all of the elements found on the gui."""
        # Window
        self.root = tk.Tk()

        # Buttons
        self.generate = tk.Button(self.root, text='Generate Message',relief=tk.RIDGE, borderwidth=2)
        self.upload = tk.Button(self.root, text='Import File', relief=tk.RIDGE, borderwidth=2)
        self.clear = tk.Button(self.root, text='Clear Output', relief=tk.RIDGE, borderwidth=2)
        self.export = tk.Button(self.root, text='Export Output', relief=tk.RIDGE, borderwidth=2)
        self.quit = tk.Button(self.root, text='Quit', height = 2, width = 6, relief=tk.RIDGE, borderwidth=2)

        # Text Boxes
        self.example = tk.Text(self.root, height=5, width=40, borderwidth=2)
        self.userInput = tk.Text(self.root,relief=tk.RIDGE, height=50, width=55, borderwidth=2)
        self.result = tk.Text(self.root, relief=tk.RIDGE, height=50, width=55, borderwidth=2)
        self.allowedSpecies = tk.Text(self.root, relief=tk.RIDGE, height=3, width=40, borderwidth=2)

        # Labels
        self.guidelines1 = tk.Label(self.root, text="""This is a graphical user interface to generate the oldest common species message.\nYou can upload a csv, json, txt, file or input your data manually into the input box.""")
        self.guidelines2 = tk.Label(self.root, text="Please input your data line-by-line with the delimiter as ',': ")
        self.allowedSpeciesLabel = tk.Label(self.root, text="Allowed Species: ")
        self.outputMessage = tk.Label(self.root, text="Ouput Message: ")


    def headerInfo(self):
        """Formats all of the header elements on the gui."""
        # Labels that detail the instructions on how to use the app.
        self.guidelines1.grid(column=0, row=0, sticky=tk.W, padx=(13, 10))
        self.guidelines2.grid(row=15, column=0, sticky=tk.W, padx=(13, 10))
        self.allowedSpeciesLabel.grid(row=3, column=2, columnspan=2, sticky=tk.E, padx=(0, 350), pady=(0, 0))
        self.outputMessage.grid(row=15, column=2 , columnspan=2)

        # Uneditable Text Box showcasing an example for the input format.
        self.example.insert(tk.END, """Manual Input Data Format:\n\t
                                        Spike,1/1/2020,white,dog\n\t
                                        Sandy,3/5/2018,blue,cat\n\t
                                        Fluffy,2/29/2016,black,sheep\n\t
                                        Garfield,9/17/1998,orange,cat\n""")
        self.example.bind("<Key>", lambda e: "break")
        self.example.grid(row=3, column=0, padx=(15, 10), sticky=tk.W)

    def buttons(self):
        """Formats all of the button elements on the gui."""
        # Generates the output message for the output Text Box by using the manual input box.
        self.generate.config(command=lambda: self.result.insert(tk.END, self.messageGeneration("Manual")))
        self.generate.grid(row=25, column=0, sticky=tk.W, pady=4, padx=(15, 10))

        # Generates the output message for the output Text Box by using allowing the user to visually upload a file.
        self.upload.config(command=lambda: self.result.insert(tk.END, self.messageGeneration("File")))
        self.upload.grid(row=25, sticky=tk.W, pady=4, padx=(150, 10))

        # Clears the output box.
        self.clear.config(command=lambda: self.result.delete(1.0,tk.END))
        self.clear.grid(row=25, column=2, columnspan=2, sticky=tk.W, pady=(0,7), padx=(0, 10))

        # Exports the generated image to a json file.
        self.export.config(command=lambda: MO.fileExport(filedialog.askdirectory(), self.result.get(1.0, tk.END)))
        self.export.grid(row=25, column=2, columnspan=2, sticky=tk.W, pady=(0,7), padx=(98, 10))

        # Destroys the gui window
        self.quit.config(command=lambda: sys.exit())
        self.quit.grid(row=0, column=2, columnspan=2, sticky=tk.E, pady=4, padx=(0, 20))

    def inputOutput(self):
        """Formats all of the interactable Text elements on the gui."""
        # User input
        self.userInput.insert(tk.END, "Spike,1/1/2020,white,dog\nSandy,3/5/2018,blue,cat\nFluffy,2/29/2016,black,sheep\nGarfield,9/17/1998,orange,cat")
        self.userInput.grid(row=20, column=0, padx=(15, 10), sticky=tk.W)

        # User output
        self.result.bind("<Key>", lambda e: "break")
        self.result.grid(row=20, column=2, columnspan=2, padx=(0, 10), sticky=tk.W)

        # User defined allowed species dictionary
        self.allowedSpecies.insert(tk.END, '{"dog" : "bark", "cat" : "meow", "sheep" : "baa"}')
        self.allowedSpecies.grid(row=3, column=2, padx=(15, 20), columnspan=2, sticky=tk.E)

    def messageGeneration(self, inputType) -> str:
        """Handles the interaction with the message_ops module and formatting the input and output taken
        from the gui.
        Args:
            inputType (str): Identifies the orgin of the function call.
        Return:
            outputString (str): Is the output from the message_ops module.
        Raises:
            - Upload fail.
        """
        self.result.delete(1.0,tk.END)
        allowedSpecies = self.allowedSpecies.get(1.0, tk.END)
        if inputType == "File":
            try:
                self.userInput.delete(1.0,tk.END)
                out = MO.fileImport(filedialog.askopenfilename(), allowedSpecies, "gui")
                self.userInput.insert(tk.END, "User uploaded a file.")
                return out
            except:
                self.userInput.insert(tk.END, "Upload fail.")
        else:
            self.result.delete(1.0,tk.END)
            return MO.manualInput(self.userInput.get(1.0, tk.END), allowedSpecies, "gui")

    def run(self, name, size):
        """Intializes and runs the gui.
        Args:
            name (str): The name of the window.
            size (str): The size of the window.
        """
        self.root.title(name)
        self.root.geometry(size)
        self.headerInfo()
        self.inputOutput()
        self.buttons()
        self.root.mainloop()
