from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Create dict to save users
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }

    # Going by users
    for user in users:
        # Make current year in users data
        current_year = date.today().year
        new_birthday = datetime(current_year,
                                user["birthday"].month,
                                user["birthday"].day
                                ).date()
        # Check if birthday was before today
        if new_birthday < date.today():
            new_birthday = datetime(current_year + 1,
                                    user["birthday"].month,
                                    user["birthday"].day
                                    ).date()

        # Determine whether the birthday falls on this week
        if date.today() <= new_birthday <= date.today() + timedelta(6):
            # Add the user to the appropriate day of the week
            if new_birthday.weekday() in [5, 6]:  # Saturday or Sunday
                birthdays_per_week["Monday"].append(user["name"])
            else:
                weekday = new_birthday.strftime("%A")
                birthdays_per_week[weekday].append(user["name"])

    # Del empty keys
    a = {}
    for key, value in birthdays_per_week.items():
        if len(value) != 0:
            a.update({key: value})
    birthdays_per_week = a

    return birthdays_per_week


if __name__ == "__main__":
    # Empty list
    # users = []

    # # Test list 1
    # users = [
    #     {"name": "July", "birthday": datetime(1982, 12, 4).date()},
    #     {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    #     {"name": "Bill", "birthday": datetime(2023, 10, 30).date()},
    #     {"name": "Jan", "birthday": datetime(2023, 11, 1).date()},
    #     {"name": "Kim", "birthday": datetime(2023, 11, 2).date()},
    # ]

    # Test list 2
    users = [
        {"name": "Sam", "birthday": datetime(1982, 12, 6).date()},
        {"name": "111", "birthday": datetime(2023, 12, 6).date()},
        {"name": "Wednesday", "birthday": datetime(2023, 12, 6).date()},
        {"name": "Thursday", "birthday": datetime(1982, 12, 7).date()},
        {"name": "Friday", "birthday": datetime(1982, 12, 8).date()},
        {"name": "Saturday", "birthday": datetime(1982, 12, 9).date()},
        {"name": "Sunday", "birthday": datetime(1982, 12, 10).date()},
        {"name": "Next_Monday", "birthday": datetime(1982, 12, 11).date()},
        {"name": "Next_Tuesday", "birthday": datetime(1982, 12, 12).date()},
        {"name": "Next_Wednesday", "birthday": datetime(1982, 12, 13).date()},
        {"name": "July", "birthday": datetime(1982, 12, 4).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill", "birthday": datetime(2023, 10, 30).date()},
        {"name": "Jan", "birthday": datetime(2023, 11, 1).date()},
        {"name": "Kim", "birthday": datetime(2023, 11, 2).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
