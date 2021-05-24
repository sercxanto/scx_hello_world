# Hello world python package example

## Development install

```shell
python3 -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

There is no need to call `pip install -r requirements-dev.txt`, thats already covered by `pip install -e .[dev]`.


## tox

tox will run tests and lint.

As tox manages its own virtual environment run **outside** of the virtual environment:

```shell
pipx install tox
tox
```

To test against multiple versions of python they need to be installed with pyenv first (remember to install tox as last command):

```shell
pyenv install 3.5.10
pyenv install 3.6.13
pyenv install 3.7.10
pyenv install 3.8.10
pyenv install 3.9.5
pyenv local 3.5.10 3.6.13 3.7.10 3.8.10 3.9.5
pipx install tox
pipx inject tox tox-pyenv
```

## pex

It is also possible to create a bundled pex package with:

```shell
tox -e package
```

The package is available in the folder `./build`.