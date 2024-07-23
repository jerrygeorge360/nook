# Nook

**Nook** is a command-line interface (CLI) application that allows you to manage key-value pairs. It provides functionality to add, delete, and retrieve key-value pairs using simple commands. This project uses the Click library for the CLI interface and pickle for data persistence. It can also be used programmatically as a libray. 

## Features

- Add key-value pairs.
- Delete key-value pairs.
- Retrieve values by key.


## Usage

- Can be used as a quick database solution in development
- Can be used to store environment keys and possibly other config keys.
## Installation
### Using pip
```sh
  pip install nook
```
### From github
To get started with nook, clone this repository and install the required dependencies.

```sh
git clone https://github.com/jerrygeorge360/nook.git
cd nook
pip install -r requirements.txt
```

## Usage 
### through the terminal
### Adding a Key-Value Pair

To add a key-value pair, use the `add` command with the `--key` (or `-k`) and `--value` (or `-v`) options.

```sh
nook add --key yourkey --value yourvalue
```

### Deleting a Key-Value Pair

To delete a key-value pair, use the `delete` command with the `--delete` (or `-d`) option.

```sh
nook delete --delete yourkey
```

### Retrieving a Value

To retrieve a value by key, use the `get_value` command with the `--getvalue` (or `-g`) option.

```sh
nook getvalue --key yourkey
```

### Programmatic usage

``` sh
from nook import add,delete,getvalue
```
```
add.callback('key','value')
```

```
getvalue.callback('key')
```

```
getvalue.callback('key')
```

```
delete.callback('key')
```
## Commands

- `add`: Adds a key-value pair to the hashmap.
  - Options:
    - `-k, --key TEXT`: Key to add.
    - `-v, --value TEXT`: Value to add.

- `delete`: Deletes a key-value pair from the hashmap.
  - Options:
    - `-k, --key TEXT`: Key to delete.

- `getvalue`: Retrieves the value for a given key.
  - Options:
    - `-k, --key TEXT`: Key to get the value for.

## Project Structure

```
.
├── main.py
├── commands.py
├── utils.py
├── hashmap.pickle
├── requirements.txt
└── README.md
```

- `main.py`: The main entry point for the CLI application.
- `commands.py`: Contains the CLI commands for the application.
- `utils.py`: Contains utility functions and classes used by the application.
- `hashmap.pickle`: File used to persist the hashmap data.
- `requirements.txt`: File listing the dependencies required for the project.
- `README.md`: This file.

## Requirements

- Python 3.6 or higher
- Click library

## License

This project is licensed under the MIT License

