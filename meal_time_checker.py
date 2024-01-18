class MealTimeChecker:
    MEAL_TIMES = {
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
        for meal, (start, end) in self.MEAL_TIMES.items():
            if start <= user_time_float <= end:
                return f"Time for {meal}"
        return "No meal time found"