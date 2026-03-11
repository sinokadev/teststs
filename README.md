# Teststs
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/teststs?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/teststs)
![PyPI - Version](https://img.shields.io/pypi/v/teststs)
![PyPI - License](https://img.shields.io/pypi/l/teststs)

No Classes, No Boilerplate, Use teststs

```bash
pip install teststs
```

PyPI: https://pypi.org/project/teststs/

## Using

```py
from teststs import teststs

def add_five(inp):
    return int(inp) + 5

tests = [
    ("5", 10),
    ("10", 15),
]

teststs(tests, add_five, detail=True)
teststs(tests, add_five, detail=False) # Default
```

If you want more usage, check out Docstring

## License

BSD-3-Clause license

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sinokadev/teststs&type=date&legend=top-left)](https://www.star-history.com/#sinokadev/teststs&type=date&legend=top-left)
