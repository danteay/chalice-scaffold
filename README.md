# Chalice scaffold

## Requirements

* Virtualenv
* `make` command

## Installing requirements

### virtualenv

Virtualenv is used to keep all project dependencies agnostic to your local installation 
by running an isolated and empty python environment, to use it you need to install it on 
Ubuntu like this:

```shell script
sudo apt install python3-virtualenv -y
```

Or directly from `pip` like this:

```shell script
pip3 install virtualenv
```

### Make command

Make is used to write simple task related to the project like format, lint and run 
locally. To install make you can run the next command:

```shell script
sudo apt install make -y
```

## Preparing environment

Once you have all requirements installed you need to prepare the project virtualenv, 
to do this follow the next commands:

```shell script
# Create a new virtualenv of python3.8
make venv

# Activate virtualenv
soruce venv/bin/activate

# Install project dependencies
make install
```

This will install all python and serverless dependencies of the project. If you want to 
start using local python installation instead of project virtualenv, just run the 
deactivate command.

## Make commands

* **Run local:** `make run` (require chalice package) Start project locally
* **Lint code:** `make lint` (requires pylint package)
* **Run tests:** `make test` (test files should be placed on tests folder)
* **Format code:** `make fmt` (requires black package)
* **Check Code Complexity:** `make complexity` (requires radon package)
* **Create Virtualenv:** `make venv` (requires virtualenv package)
* **Install dependencies:** `make install` (install pylint, radon, black and requirements.txt 
  packages)
