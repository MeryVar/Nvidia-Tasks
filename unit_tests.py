import unittest
from meal_time_checker import MealTimeChecker
from game_build_meta_information import update
from plate_validator import PlateValidator


class TestMealTimeChecker(unittest.TestCase):

    def setUp(self):
        self.meal_checker = MealTimeChecker()

    def test_time_convert_to_float(self):
        self.assertEqual(self.meal_checker.time_convert_to_float("07:30"), 7.5)
        self.assertEqual(self.meal_checker.time_convert_to_float("12:15"), 12.25)
        self.assertEqual(self.meal_checker.time_convert_to_float("18:45"), 18.75)

    def test_check_meal_times_breakfast(self):
        self.assertEqual(self.meal_checker.check_meal_times("07:30"), "Time for breakfast")
        self.assertEqual(self.meal_checker.check_meal_times("07:00"), "Time for breakfast")

    def test_check_meal_times_lunch(self):
        self.assertEqual(self.meal_checker.check_meal_times("12:30"), "Time for lunch")
        self.assertEqual(self.meal_checker.check_meal_times("12:00"), "Time for lunch")

    def test_check_meal_times_dinner(self):
        self.assertEqual(self.meal_checker.check_meal_times("18:45"), "Time for dinner")
        self.assertEqual(self.meal_checker.check_meal_times("19:00"), "Time for dinner")

    def test_check_meal_times_no_meal_time(self):
        self.assertEqual(self.meal_checker.check_meal_times("10:00"), "No meal time found")
        self.assertEqual(self.meal_checker.check_meal_times("14:00"), "No meal time found")
        self.assertEqual(self.meal_checker.check_meal_times("20:00"), "No meal time found")

    def test_check_meal_times_invalid_time_format(self):
        self.assertEqual(self.meal_checker.check_meal_times("invalid"), "Invalid time format. Use *:*, *:** or **:**)")
        self.assertEqual(self.meal_checker.check_meal_times("25:00"), "Invalid time format. Use *:*, *:** or **:**")


class TestGameBuildMetaInformation(unittest.TestCase):

    def test_append_values(self):
        initial_meta = {}
        update(initial_meta, "append", "namespace1", ["value1", "value2"])
        self.assertEqual(initial_meta, {"namespace1": {1: ["value1", "value2"]}})

    def test_append_values_with_type(self):
        initial_meta = {}
        update(initial_meta, "append", "namespace1", ["value1", "value2"], type_=2)
        self.assertEqual(initial_meta, {"namespace1": {2: ["value1", "value2"]}})

    def test_delete_values(self):
        initial_meta = {"namespace1": {1: ["value1", "value2"]}}
        update(initial_meta, "delete", "namespace1", ["value1"])
        self.assertEqual(initial_meta, {"namespace1": {1: ["value2"]}})

    def test_delete_values_with_type(self):
        initial_meta = {"namespace1": {2: ["value1", "value2"]}}
        update(initial_meta, "delete", "namespace1", ["value1"], type_=2)
        self.assertEqual(initial_meta, {"namespace1": {2: ["value2"]}})


class TestPlateValidator(unittest.TestCase):

    def test_valid_plate(self):
        validator = PlateValidator("AB123")
        self.assertTrue(validator.is_plate_valid())

    def test_invalid_length(self):
        validator = PlateValidator("A")
        self.assertFalse(validator.is_plate_valid())

    def test_invalid_start_with_numbers(self):
        validator = PlateValidator("123AB")
        self.assertFalse(validator.is_plate_valid())

    def test_invalid_characters(self):
        validator = PlateValidator("AB-123")
        self.assertFalse(validator.is_plate_valid())

    def test_invalid_end_with_zero(self):
        validator = PlateValidator("AB120")
        self.assertFalse(validator.is_plate_valid())

    def test_invalid_contains_whitespace(self):
        validator = PlateValidator("AB 123")
        self.assertFalse(validator.is_plate_valid())

    def test_invalid_contains_punctuation(self):
        validator = PlateValidator("AB,123")
        self.assertFalse(validator.is_plate_valid())


if __name__ == '__main__':
    unittest.main()