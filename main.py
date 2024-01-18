from meal_time_checker import MealTimeChecker
from game_build_meta_information import update, load_json, save_json
from plate_validator import PlateValidator


def main():
    print("Choose an option:")
    print("1. Meal Time Checker")
    print("2. Game Build Meta Information")
    print("3. Plate Validator")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        main_meal_time_checker()
    elif choice == "2":
        main_game_build_meta_information()
    elif choice == "3":
        main_plate_validator()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


def main_meal_time_checker():
    meal_checker = MealTimeChecker()
    user_time = input("Enter the time *:*, *:** or **:**): ")
    result = meal_checker.check_meal_times(user_time)
    print(result)


def main_game_build_meta_information():
    json_file_path = input("Enter the path to the JSON file: ")
    meta = load_json(json_file_path)

    command = input("Enter command (append/delete): ")
    namespace = input("Enter namespace: ")
    values = input("Enter values (comma-separated): ").split(',')
    type_ = int(input("Enter type (default is 1): ") or 1)

    update(meta, command, namespace, values, type_)

    output_file_path = input("Enter the path to save the updated JSON file: ")
    save_json(output_file_path, meta)
    print("Updated Meta Information:", meta)


def main_plate_validator():
    plate = input("Enter the plate: ")
    validator = PlateValidator(plate)
    if validator.is_plate_valid():
        print("Plate is valid.")
    else:
        print("Plate is not valid.")


if __name__ == '__main__':
    main()