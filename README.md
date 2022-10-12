# Arguing
Arguing is a Lightweight and simple **Argument parsing** library that gives you all the control, no third party libraries.


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
    '--argument',  # Argument name.
    type=str,  # Type of the argument, by default string.
    default='default_value',  # If the user don't pass the flag or it doesn't have a value, it will be automatically setted to this. 
    help='Help.'  # Help message
    # You can also add Mandatory arguments witht the "mandatory" parameter (Bool)!
)
# Also, you can define a variable to the function and it will return the argument value.

arguing.get('--argument')
# arguing.get() returns the parameters value
# It will return it converted to the selected type on arguing.set() if used
# If arguing.get() can't get the parameters value, it will return the default on arguing.set() or None.

# In case you wan't to check if the user passed an specific argument you can use:
arguing.check('--argument') # Checks if argument is on ARGV and if it has a value, returns Bool.


print(arguing.get('--argument'))
print(argument)
# Both are valid
```

# What's new
- \[Fixed bug\] `.check()` would return `True` even if the flag does not have any value.
- \[Fixed bug\] When adding flag without a value, raises `IndexError`. Should return it's default value or None.