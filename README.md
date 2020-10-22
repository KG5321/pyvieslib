# PyVIESLib

PyVIESLib is a Python library for validating VIES numbers

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyvieslib.

```bash
pip install pyvieslib
```

## Usage

```python
from pyvieslib import PyViesLib

vvl = PyViesLib()
vvl.check_vies("PL1234567890") # returns False
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## TODO
* Write proper tests
* Finish validators for all countries

## License
[MIT](https://choosealicense.com/licenses/mit/)
