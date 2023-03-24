# Guessing songs

## Prerequisites

Install bazel

```bash
brew install bazelisk
```

## Running the app locally

```bash
bazel run //server:app
```

Then see the webpage at: http://127.0.0.1:5000/

## Debugging guide

In app.py, uncomment this line

```python
import debugpy; debugpy.listen(5724); debugpy.wait_for_client()
print("Please start debugging client from VSCODE")
```

Then run the app locally as in [Running the app locally](#running-the-app-locally)

Then run and debug `Python: Attach` from VSCode

## Enable auto-completion in local VSCode workspace

First, enable venv environment for python 3.9.16

1. Install pyenv

```
brew install pyenv
```

```
pyenv init
```

And follow the instruction to add into `~/.zshrc`

2. Install 3.11.2

```
pyenv install 3.11.2
pyenv global 3.11.2
```

3. Create venv environment 

```
python -m venv ./venv
```

4. Activate the environment

```
. ./venv/bin/activate
```

5. Install dependencies

```
pip install -r requirements_lock.txt
```

Then in VSCode with Python extension enabled we should see auto-completion in code