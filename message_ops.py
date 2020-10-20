"""This module handles all of the core logic when determining the oldest common animal"""
import re
import json
import datetime

class Animal:
    """Animal to represent each datapoint input in by the user."""
    def __init__(self, _name, _dateOfBirth, _color, _species) -> None:
        """Initializes parameters for the attributes of the Animal Class.
        Args:
            _name (str): Name of the Animal.
            _dateOfBirth (str): The date of birth for the Animal.
            _color (str): The color of the Animal.
            _species (str): The Animal's species.
        """
        self.name = _name
        self.dateOfBirth = _dateOfBirth
        self.color = _color
        self.species = _species

class AnimalDict:
    """The Animal Dictionary class is responsible for holding a list of all of the datapoints
    input in by the user and are allowed species. Then generating the oldest common
    ancestor in the form output message. Parts of this classes error handaling is based off
    of the interface being used which can be either command line or a graphical user."""
    def __init__(self, _allowedSpecies = None, _interface = "cli") -> None:
        """Initializes parameters for the attributes of the Animal Dictionary class.
        Args:
            _allowedSpecies (dict): A dictionary containing the allowed species as the keys
                and the values as the sound the animal makes.
            _interface (str): Indicates what type of interface the user is using this class from.
        """
        self.species = _allowedSpecies if _allowedSpecies else dict()
        self.interface = _interface
        self.message = "" # This is where the output message will be stored.
        self.maps = dict() # This will contain all of the Animal Objects.

    def addAnimal(self, _animal) -> None:
        """Adds an Animal Object to the maps attribute which holds all of the datapoints input by
        the user as well as keeps track of the oldest Animal object for each species. If a species
        is not found within the maps attribute the user will be alerted to this and be required to
        add that species into their allowedSpecies dictionary.
        Args:
            _animal (Animal): An Animal Object being requested to be added to the maps attribute.
        """
        # Species error handling
        if not self.species.get(_animal.species) and self.interface == "cli":
            response = input(f"Would you like to add {_animal.species} Allowed Species [Y/N]: ")
            if re.match('^[Yy].*', response):
                self.addSpecies({_animal : input(f"What sound does a {_animal.species} makes: ")})
            else:
                return
        elif not self.species.get(_animal.species):
            self.message = f'"{_animal.species}" is not in Allowed Species.\n' + self.message
            return

        # Oldest animal update and adding animal to maps["Members"].
        if self.maps.get(_animal.species):
            animal_DOB = _animal.dateOfBirth.split('/')
            oldestCommon_DOB = self.maps[_animal.species]['Oldest'].dateOfBirth.split('/')
            if datetime.date(int(animal_DOB[2]), int(animal_DOB[0]), int(animal_DOB[1])) < datetime.date(int(oldestCommon_DOB[2]), int(oldestCommon_DOB[0]), int(oldestCommon_DOB[1])):
                self.maps[_animal.species]['Oldest'] = _animal
            self.maps[_animal.species]['Members'].append(_animal)
        else:
            self.maps[_animal.species] = {'Oldest': _animal, 'Members':[_animal]}

    def addSpecies(self, _species) -> None:
        """Adds a species to the allowedSpecies attribute which holds all of the allowed species
        that can be input into the maps attribute. Each species is mapped the species' sound.
        Args:
            _species (dict): The key is the species and this is mapped to the species' sound.
        """
        self.species.update(_species)

    def oldestCommon(self) -> str:
        """Gets the oldest common animal within the maps attribute by first getting the longest list
        of Animals among all of the species and then getting the 'Oldest' Attribute from that
        species. Finally constructs the message from the oldest common animal and both returns the
        string and sets it equal to the message attribute.
        Returns:
            self.message (str): The constructed message from the oldest common animal.
        """
        if self.message == "":
            longestSublist, oldestCommon = max(len(species['Members']) for species in self.maps.values()), None
            listOfObjects = [species['Oldest'] for species in self.maps.values() if len(species['Members']) == longestSublist]
            for animal in listOfObjects:
                if not oldestCommon:
                    oldestCommon = animal
                else:
                    animalDOB = animal.dateOfBirth.split('/')
                    oldestCommonDOB = oldestCommon.dateOfBirth.split('/')
                    if datetime.date(int(animalDOB[2]), int(animalDOB[0]), int(animalDOB[1])) < datetime.date(int(oldestCommonDOB[2]), int(oldestCommonDOB[0]), int(oldestCommonDOB[1])):
                        oldestCommon = animal
            self.message = f'{oldestCommon.name}, the {oldestCommon.color} {oldestCommon.species} says {self.species[oldestCommon.species]}!'
        return self.message

def manualInput(_inputString, _allowedSpecies = None, _interface = "cli") -> str:
    """Parses the input string which is then used to intialize the Animal Dictionary. After
    all of the data has been passed, the Animal Dictionary's oldestCommon method is used to
    generate the output string.
    Args:
        _inputString (str): A string that has been manually inputted in by the user.
        _allowedSpecies (dict): A dictionary containing the allowed species as the keys
            and the values as the sound the animal makes.
        _interface (str): Indicates what type of interface the user is using this function from.
    Returns:
        Output_String (str): This string can be the expected output string or an error messages.
    Raises:
        - Invalid Allowed Species Input
        - Invalid Input Format
    """
    # Makes sure the Allowed Species dictionary input is valid.
    try:
        if not _allowedSpecies:
            Primary = AnimalDict({'dog' : 'bark', 'cat' : 'meow','sheep' : 'baa'}, _interface)
        else:
            Primary = AnimalDict(json.loads(_allowedSpecies),  _interface)
    except:
        return "Invalid Allowed Species Input"

    # Intializes and generates the Oldest Common Animal.
    try:
        _inputString = _inputString.strip().split('\n')
        _ = [Primary.addAnimal(Animal(*d.strip('\n').strip().split(','))) for d in _inputString]
        Primary.oldestCommon()
        return Primary.message
    except:
        return "Invalid Input Format"

def fileImport(_path, _allowedSpecies = None, _interface = "cli") -> str:
    """Parses the input string which is then used to intialize the Animal Dictionary. After
    all of the data has been passed, the Animal Dictionary's oldestCommon method is used to
    generate the output string.
    Args:
        _path (str): The path to the file to be imported.
        _allowedSpecies (dict): A dictionary containing the allowed species as the keys
            and the values as the sound the animal makes.
        _interface (str): Indicates what type of interface the user is using this function from.
    Returns:
        Output_String (str): This string can be the expected output string or an error messages.
    Raises:
        - Invalid Allowed Species Input
        - Invalid Input Format
        - Unsupported File Type (gui currently)
    """
    # Makes sure the Allowed Species dictionary input is valid.
    try:
        if not _allowedSpecies:
            Primary = AnimalDict({'dog' : 'bark', 'cat' : 'meow', 'sheep' : 'baa'},  _interface)
        else:
            Primary = AnimalDict(json.loads(_allowedSpecies),  _interface)
    except:
        return "Invalid Allowed Species Input"
    filetype = _path.split(".")[-1]
    if filetype in ["json", "csv", "txt"]:
        try:
            if filetype == "json":
                fptr = json.load(open(_path, 'r'))
                _ = [Primary.addAnimal(Animal(*list(d.values()))) for d in fptr]
            elif filetype == "csv":
                fptr = open(_path, 'r').readlines()[1:]
                _ = [Primary.addAnimal(Animal(*d.strip('\n').strip().split(","))) for d in fptr]
            elif filetype == "txt":
                fptr = open(_path, 'r').readlines()
                _ = [Primary.addAnimal(Animal(*d.strip('\n').strip().split(","))) for d in fptr]
        except:
            return "Invalid Input Format"
    else:
        return "Unsupported File Type"
    Primary.oldestCommon()
    return Primary.message

def fileExport(_path, _outputString) -> None:
    """This will pipe the output of this program to a json file containing the Animal information.
    Args:
        _path (str): The path to the file to be exported.
        _outputString (str): The constructed message from the oldest common animal.
    """
    Output_Dict = _outputString.split(" ")
    Output_Json = {"Name": Output_Dict[0][0:-1],
                   "Color": Output_Dict[2],
                   "Species": Output_Dict[3],
                   "Sound" : Output_Dict[5][0:-1],
                   "Message" : _outputString}
    json.dump(Output_Json, open(_path+"/"+Output_Json["Name"]+".json", "w"))
