# Arguing
Arguing is a little library who lets you create a nice CLI without bloating your app.<br>
Arguing doesn't needs you defining every argument that you wan't, just get it.

# Installation
You can use PIP or GIT to install the library, both are the same version.
```
pip install arguing
git clone https://github.com/ZSendokame/arguing
```

# Use
After installing the library, here's a brief tutorial.
```py
import arguing

arguing.setArgument('--argument') # To specify a type for the argument value, use the parameter "argumentType", like
arguing.setArgument('--argument', argumentType=int) # For example, Converts to int.

# arguing.setArgument() is for mandatory arguments, in case you don't need a mandatory argument you can just get it with
arguing.getArgument('--argument') # Work with mandatory and not mandatory arguments.

# In case you wan't to check if the user passed an specific argument you can use
arguing.checkArgument('--argument') # Return True or False.
```