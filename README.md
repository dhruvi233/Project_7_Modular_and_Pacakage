🧰 Project 7: Python Multi-Utility Toolkit
Modular Programming and Packages
Overview
The Python Multi-Utility Toolkit is a menu-driven application that brings together date and time tools, mathematical calculations, random generators, UUID creation, and basic file operations. It demonstrates how to organize a Python application using built-in modules, custom modules, and packages.

Video Demonstration
Video Link: (https://drive.google.com/file/d/1FX9jhQ3Fj_CPAJJbmR9VT1bqmiOY7Ouv/view?usp=sharing)
In the demonstration, introduce the project, explain the folder structure and imports, then run the program and show selected menu options.

Objectives
•	Practice importing and using Python built-in modules.
•	Create reusable custom modules and packages with __init__.py files.
•	Use a menu-driven interface to organize multiple utilities.
•	Perform basic file creation, reading, writing, and appending.
•	Explore module attributes dynamically and understand the __name__ == '__main__' pattern.

Features
•	Date and time utilities: current date/time, date differences, custom formatting, stopwatch, and countdown.
•	Math utilities: arithmetic and advanced calculations, factorials, logarithms, trigonometry, compound interest, and geometry areas.
•	Random utilities: random numbers and choices, sampling, password/OTP generation, and dice or game simulations.
•	UUID utility: generate a UUID version 4 identifier.
•	File utilities: create, write, read, and append to files.
•	Custom geometry modules for circle, rectangle, and triangle area calculations.
•	Dynamic module exploration using dir().
•	Input validation and a menu-driven console interface.

Python Concepts Used
•	Built-in modules: datetime, time, math, random, uuid, string, and importlib.
•	Custom modules and packages.
•	Imports and package initializers (__init__.py).
•	Functions, parameters, return values, and exceptions.
•	Pathlib and text file operations.
•	Loops, conditional statements, and menu-driven programming.
•	Input validation and error handling.
•	dir() for module exploration.
•	The __name__ == '__main__' entry-point pattern.

Program Menu
The main menu groups the toolkit into options such as:
•	Date and Time Tools
•	Mathematical Tools
•	Random Number, Password, OTP, and Dice Tools
•	File Operations
•	Module Explorer
•	UUID Generator
•	Exit

Menu labels may differ slightly depending on the final version of main.py.
Sample Program Output
====================================
      PYTHON MULTI-UTILITY TOOLKIT
====================================
1. Date and Time Tools
2. Mathematical Tools
3. Random Utilities
4. File Operations
5. Explore Modules
6. Generate UUID
0. Exit
Enter your choice: 6
Generated UUID: <a UUID4 value is displayed here>

Input Validation Rules
•	Numeric inputs should be entered in the requested format.
•	Negative values are rejected where a calculation requires a non-negative measurement or value.
•	Factorial accepts non-negative integers only.
•	File operations validate filenames to help prevent paths outside the intended working folder.
•	If an invalid choice or value is entered, follow the message shown by the program and try again.

How to Run
1.	Install Python 3 if it is not already installed.
2.	Download or clone the repository and open the project folder in VS Code or a terminal.
3.	Ensure package folders and their Python files are kept in the correct structure.
4.	Open a terminal in the project root folder.
5.	Run: python main.py
6.	Choose a menu option and follow the on-screen prompts.

Program Structure
Project_7/
├── main.py
├── greet.py
├── helper.py
├── string_utils.py
├── utilities/
│   ├── __init__.py
│   ├── file_utils.py
│   └── math_utils.py
├── shapes/
│   ├── __init__.py
│   ├── circle.py
│   └── rectangle.py
├── geometry/
│   ├── __init__.py
│   └── triangle.py
└── README.md

Assumptions
•	The application is intended to run locally in a Python 3 environment.
•	No third-party packages are required for the described core features.
•	File operations use the program's current working directory unless otherwise specified.
•	Sample output is illustrative; generated times, random values, OTPs, passwords, and UUIDs will vary.

Future Enhancements
•	Add automated unit tests for each utility module.
•	Improve the interface with clearer formatting or a graphical user interface.
•	Add logging and more detailed error messages.
•	Add configuration options for date formats and file locations.
•	Expand the toolkit with additional converters and productivity tools.

Author
Dhruvi Das

License
This project is created for educational and portfolio purposes. Add a specific open-source license if you intend to distribute or reuse the code under formal license terms.
