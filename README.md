# Arguing
Arguing is a little library who lets you create a nice CLI without bloating your app.<br>
Arguing doesn't needs you defining every argument that you wan't, just get it.

# Installation
You can use PIP to install the library.
```sh
pip install arguing
```

# Use
After installing the library, here's a brief tutorial.
```py
import arguing

arguing.set('--argument', argumentType=str, default='defaultValue')
# arguing.set() is for mandatory arguments ( You can use it for non-mandatory arguments, setting it's default value. ).
# The first parameter is the argument
# argumentType is for the type of variable that return on get()
# default sets a default value in case the user don't pass the argument.

arguing.get('--argument') # Work with mandatory and not mandatory arguments.
# arguing.get() returns the parameters value
# It will return it converted to the selected type on arguing.set() if used
# If arguing.get() can't get the parameters value, it will return the default on arguing.set() or None.

# In case you wan't to check if the user passed an specific argument you can use:
arguing.check('--argument') # Checks if argument is on ARGV, returns Bool.
```