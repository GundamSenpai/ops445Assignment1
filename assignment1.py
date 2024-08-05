#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Summer 2024
Program: assignment1.py 
The python code in this file is original work written by
"Sabeer Sekhon". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Sabeer Sekhon
Description: Assignment 1 variant C
'''

import sys

def day_of_week(date_str: str) -> str:
    """Determine the day of the week for a given date using Tomohiko Sakamoto's algorithm"""
    day, month, year = (int(part) for part in date_str.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    month_offsets = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    week_day = (year + year // 4 - year // 100 + year // 400 + month_offsets[month] + day) % 7
    return days[week_day]

def leap_year(year: int) -> bool:
    """Return true if the given year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Returns the maximum number of days in a given month, considering leap years"""
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return month_days[month]

def after(date_str: str) -> str:
    """Return the date of the next day in DD/MM/YYYY format"""
    day, month, year = (int(part) for part in date_str.split('/'))
    day += 1

    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    return f"{day:02}/{month:02}/{year}"

def before(date_str: str) -> str:
    """Return the date of the previous day in DD/MM/YYYY format"""
    day, month, year = (int(part) for part in date_str.split('/'))
    day -= 1

    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)
    
    return f"{day:02}/{month:02}/{year}"

def usage():
    """Print a usage message to the user"""
    print(f"Usage: {sys.argv[0]} DD/MM/YYYY NN")
    sys.exit()

def valid_date(date_str: str) -> bool:
    """Check if the given date string is valid"""
    try:
        day, month, year = (int(part) for part in date_str.split('/'))
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= mon_max(month, year)):
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date: str, days_count: int) -> str:
    """Iterate from start date by a given number of days and return the end date"""
    current_date = start_date
    for _ in range(abs(days_count)):
        if days_count > 0:
            current_date = after(current_date)
        else:
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        usage()

    input_date = sys.argv[1]
    if not valid_date(input_date):
        usage()

    try:
        days_to_iterate = int(sys.argv[2])
    except ValueError:
        usage()

    result_date = day_iter(input_date, days_to_iterate)
    print(f'The end date is {day_of_week(result_date)}, {result_date}.')
