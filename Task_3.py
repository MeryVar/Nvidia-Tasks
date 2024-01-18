class PlateValidator:
    def __init__(self, plate):
        self.plate = plate

    def has_valid_length(self):
        return 2 <= len(self.plate) <= 6

    def starts_with_two_letters(self):
        return self.plate[:2].isalpha()

    def contains_valid_characters(self):
        return self.plate.isalnum()

    def ends_with_valid_number(self):
        return self.plate[-1].isdigit() and self.plate[-1] != '0'

    def no_whitespace_or_punctuation(self):
        return not any(char.isspace() or char in ",.!?()[]{};:'\"<>-_" for char in self.plate)

    def is_plate_valid(self):
        conditions = [
            self.has_valid_length(),
            self.starts_with_two_letters(),
            self.contains_valid_characters(),
            self.ends_with_valid_number(),
            self.no_whitespace_or_punctuation()
        ]
        return all(conditions)


plate_input = input("Enter the personalized plate: ")
plate_validator = PlateValidator(plate_input)

if plate_validator.is_plate_valid():
    print("Valid plate!")
else:
    print("Sorry, invalid plate")