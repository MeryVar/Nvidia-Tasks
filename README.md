# Python Script with Three Functionalities

This Python script provides three functionalities: Meal Time Checker, Game Build Meta Information, and Plate Validator.

## Table of Contents

- [Meal Time Checker](#meal-time-checker)
- [Game Build Meta Information](#game-build-meta-information)
- [Plate Validator](#plate-validator)
- [Usage](#usage)

## Meal Time Checker

This functionality checks whether a given time corresponds to breakfast, lunch, or dinner.

### How to Use

1. Run the script.
2. Choose option 1 for Meal Time Checker.
3. Enter a time in the format
   - `*:*`
   - `*:**`
   - `**:**`
4. View the result indicating the meal time.

## Game Build Meta Information

This functionality updates JSON meta information for a game build.

### How to Use

1. Run the script.
2. Choose option 2 for Game Build Meta Information.
3. Enter the path to the JSON file containing meta information.
4. Choose between "append" and "delete" commands.
5. Enter the namespace, values, and type.
6. Enter the path to save the updated JSON file.

## Plate Validator

This functionality validates personalized plates.

### How to Use

1. Run the script.
2. Choose option 3 for Plate Validator.
3. Enter a personalized plate.
4. View the result indicating whether the plate is valid or not.

## Usage

1. Make sure to have Python installed on your system.
2. Create a virtual environment using the following commands:

   ```bash
   python -m venv venv
   
3. Activate the virtual environment:
- `On Windows`:

  ```bash
  .\venv\Scripts\activate

- `On macOS and Linux`:
   
   ```bash
   source venv/bin/activate

4. Once the virtual environment is activated, install the dependencies:
   ```bash
   pip install -r requirements.txt

5. Run the script using the following command:
   ```bash
   python main.py