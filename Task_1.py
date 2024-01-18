class MealTimeChecker:
    def __init__(self):
        self.meal_times = {
            "breakfast": (7.0, 8.0),
            "lunch": (12.0, 13.0),
            "dinner": (18.0, 19.0)
        }

    @staticmethod
    def time_convert_to_float(time_str):
        time_parts = time_str.split(':')
        if len(time_parts[0]) == 1:
            time_str = '0' + time_str
        hours, minutes = map(int, time_str.split(':'))
        return hours + minutes / 60

    def check_meal_times(self, user_time):
        user_time_float = self.time_convert_to_float(user_time)
        for meal, (start, end) in self.meal_times.items():
            if start <= user_time_float <= end:
                print(f"Time for {meal}")
                return


user_time_input = input("Enter the time in *:*, *:** or **:** format: ")
meal_checker = MealTimeChecker()
meal_checker.check_meal_times(user_time_input)
