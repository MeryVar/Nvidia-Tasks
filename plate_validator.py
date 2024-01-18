class PlateValidator:
    def __init__(self, plate: str):
        self.plate: str = plate

    def has_valid_length(self) -> bool:
        return 2 <= len(self.plate) <= 6

    def starts_with_two_letters(self) -> bool:
        return self.plate[:2].isalpha()

    def contains_valid_characters(self) -> bool:
        return self.plate.isalnum()

    def ends_with_valid_number(self) -> bool:
        return self.plate[-1].isdigit() and self.plate[-1] != '0'

    def no_whitespace_or_punctuation(self) -> bool:
        return not any(char.isspace() or char in ",.!?()[]{};:'\"<>-_" for char in self.plate)

    def is_plate_valid(self) -> bool:
        conditions = [
            self.has_valid_length(),
            self.starts_with_two_letters(),
            self.contains_valid_characters(),
            self.ends_with_valid_number(),
            self.no_whitespace_or_punctuation()
        ]
        return all(conditions)