# Teststs
A Simple, Tiny Test Library for Python

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

## License

BSD-3-Clause license

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sinokadev/teststs&type=date&legend=top-left)](https://www.star-history.com/#sinokadev/teststs&type=date&legend=top-left)
