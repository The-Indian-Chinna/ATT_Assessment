# AT&T Assessment: Oldest Common Animal

This is a python app that accepts a list of animals with the feilds name,date of birth,color, species and outputs the oldest common Animal from the input list. This App supports interfacing via the command line interface, a graphical interface or the function itself.

input:
```txt
Spike,1/1/2020,white,dog
Sandy,3/5/2018,blue,cat
Fluffy,2/29/2016,black,sheep
Garfield,9/17/1998,orange,cat
```

output:
```txt
Garfield, the orange cat says meow!
```

## Input Formats

**Command Line Manual Input**: Each Animal is inputed with the delimeter '\n' and the delimeter for each Animal is ',' as seen below:
```txt
Spike,1/1/2020,white,dog\nSandy,3/5/2018,blue,cat\nFluffy,2/29/2016,black,sheep\nGarfield,9/17/1998,orange,cat
```

**GUI Manual Input**: Each Animal is one line and the delimeter for each Animal is ',' as seen below:
```txt
Spike,1/1/2020,white,dog
Sandy,3/5/2018,blue,cat
Fluffy,2/29/2016,black,sheep
Garfield,9/17/1998,orange,cat
```

**File Input: JSON**: Each Animal is a object with the feilds being name, date_of_birth, color and species as seen below:
```json
[
 {
   "name": "Spike",
   "date_of_birth": "1/1/2020",
   "color": "white",
   "species": "dog"
 },
 {
   "name": "Sandy",
   "date_of_birth": "3/5/2018",
   "color": "blue",
   "species": "cat"
 },
 {
   "name": "Fluffy",
   "date_of_birth": "2/29/2016",
   "color": "black",
   "species": "sheep"
 },
 {
   "name": "Garfield",
   "date_of_birth": "9/17/1998",
   "color": "orange",
   "species": "cat"
 }
]
```

**File Input: CSV**: Each Animal is one line with the columns being name, date_of_birth, color and species as seen below:
```csv
name,date_of_birth,color,species
Spike,1/1/2020,white,dog
Sandy,3/5/2018,blue,cat
Fluffy,2/29/2016,black,sheep
Garfield,9/17/1998,orange,cat
```

**File Input: TXT**: Each Animal is one line and the delimeter for each Animal is ',' as seen below:
```txt
name,date_of_birth,color,species
Spike,1/1/2020,white,dog
Sandy,3/5/2018,blue,cat
Fluffy,2/29/2016,black,sheep
Garfield,9/17/1998,orange,cat
```


## Usage

To utilize the command line interface with manual input:
```bash
python3 main.py
```

To utilize the command line interface with file input:
```bash
python3 main.py --path=path/to/inputfile
```

To utilize the graphical user interface:
```bash
python3 main.py --interface=gui
```

You can test these commands with the example files provided.