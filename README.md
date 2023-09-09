# Bored API Wrapper and Database.
This program uses a Bored API wrapper and a database class to get a random activity and save it in a database.

## Installation
1. Make sure you have Python and pip installed on your computer. You can check this by opening a command prompt and entering `python --version` and `pip --version`. If you do not have Python and pip installed, you can download them from the official Python website.

2. Clone this repository to your computer.

3. Open a command prompt and navigate to the directory where the cloned repository is located.

4. Install all dependencies by using the command `pip install -r requirements.txt`.

## Usage
To run the program, use the command `python src/main.py` with the appropriate parameters.

The program has two commands: `new` and `list`.

### The `new` command gets a random activity from the Bored API using the provided filters and saves it in the database. For example:
### python src/main.py new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5
This command will run the program and get a new random activity with type education, 1 participant, price 0.1, and accessibility 0.1, then save it in the database.

### The `list` command lists the latest activities saved in the database. For example:
### python src/main.py list
This command will run the program and list the last 5 activities saved in the database.

## Testing

To run tests for this program, use the command `python -m unittest discover` in the project directory.
