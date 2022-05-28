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

# arguing.set() is for mandatory arguments, in case you don't need a mandatory argument you can just get it with:
arguing.get('--argument') # Work with mandatory and not mandatory arguments.

# In case you wan't to check if the user passed an specific argument you can use:
arguing.check('--argument') # Return True or False.
```