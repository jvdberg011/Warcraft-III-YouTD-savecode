# Warcraft-III-YouTD-savecode

Python Script to designed for QoL improvements to users playing the Warcraft III custom map YouTD.

Script enables automatic read of the savecode.txt file and copies the users "-load" code to the clipboard for seamless paste within game.

# INITIAL SETUP

1.  Save the following file to directory of your choice:  "wc3_youtd_savecode.py".
2.  Open script with your choice of editor.
3.  Edit line 10 of script, replacing 'C:\\...\\savecode.txt' with the full filepath to your stored "savecode.txt"
4.  Save and Exit.


# REQUIRED PACKAGES/MODULES

NOTE 1:	Script imports modules from a variety of sources and will not function if these modules are not installed.

Required Python Modules:
1.	os
2.	re
3.	pyperclip

# INSTRUCTIONS TO INSTALL PYTHON MODULES/PACKAGES

PYTHON module/package installation:
1.  Open terminal.
2.  Type "pip install [insert module name]".
3.  Repeat step 2 until all required modules have been installed.

# INSTRUCTIONS FOR USE WITH ELGATO STREAM DECK

1.	Create a "System:  Open" button.
2.	Enter a "title" of your choice.
3.	Press the "Select a file..." button.
4.	Navigate to the filepath of your "wc3_youtd_savecode.py" script
5.	Press the "Open" button.

# OPERATION

1.	Run the script from CMD line, OR
2.	Run the script from an Elgato Stream Deck, as outlined above, OR
3.	Run the script from file explorer.
