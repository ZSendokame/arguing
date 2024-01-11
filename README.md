# Arguing
Arguing is a Lightweight and simple **Argument parsing** library that gives you all the control, no third party libraries.<br>
***Not uploading to PyPi, for now***

[![PyPi Version](https://img.shields.io/pypi/v/arguing.svg?logo=pypi&logoColor=yellow)](https://pypi.org/project/arguing)
[![PyPi Downloads](https://img.shields.io/pypi/dm/arguing?logo=pypi&logoColor=yellow)](https://pypistats.org/packages/arguing)

# Installation
You can use PIP to install the library.
```sh
pip install arguing

# Or, from the latest version on GitHub

pip install git+https://github.com/ZSendokame/arguing.git

```

# Use
After installing the library, here's a brief tutorial.
```py
from arguing import Arguing

args = Arguing('Help message goes here!')
argument = arguing.set(
    name='--argument',  # Argument name.
    flag=False,  # If set to true, it will return if the flag is present instead of the user input.
    type=str,  # Type of the argument, by default string.
    default=None  # If not a flag, but still has no value, returns this.
    required=False  # For required arguments/flags. If the user did not use it, exits with the help message.
)
# Also, you can define a variable to the function and it will return the value.

print(arguing.get('--argument'))  # Another way of obtaining the argument/flag value! not recommended though.
print(argument)
```