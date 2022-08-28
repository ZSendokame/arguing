# Arguing
Arguing is a little library who lets you create a nice CLI without bloating your app.<br>
Get what you want with the name you want!

[![PyPi Version](https://img.shields.io/pypi/v/arguing.svg?logo=pypi&logoColor=yellow)](https://pypi.org/project/arguing)
[![PyPi Downloads](https://img.shields.io/pypi/dm/arguing?logo=pypi&logoColor=yellow)](https://pypistats.org/packages/arguing)

# Installation
You can use PIP to install the library.
```sh
pip install arguing
```

# Use
After installing the library, here's a brief tutorial.
```py
import arguing

argument = arguing.set(
    '--argument',
    argument_type=str,
    default='default_value',
    help_message='Help.'
)
# The first parameter is the argument.
# argument_type is for the type of variable that return on get().
# default sets a default value in case the user don't pass the argument.
# Also, you can define a variable to the function and it will return the argument value.

arguing.get('--argument') # Work with mandatory and non-mandatory arguments.
# arguing.get() returns the parameters value
# It will return it converted to the selected type on arguing.set() if used
# If arguing.get() can't get the parameters value, it will return the default on arguing.set() or None.

# In case you wan't to check if the user passed an specific argument you can use:
arguing.check('--argument') # Checks if argument is on ARGV, returns Bool.
```

# What's new
- \[Fixed bug\] When adding flag without a value, raises `IndexError`. Should return it's default value or None.
- \[Removed\] Documentation function.