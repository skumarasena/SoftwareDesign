
from datetime import datetime

def get_day():
    """Returns the current day of the week."""
    d = datetime.weekday(datetime.today())
    if d == 0:
        return 'Monday'
    elif d == 1:
        return 'Tuesday'
    elif d == 2: 
        return 'Wednesday'
    elif d == 3:
        return 'Thursday'
    elif d == 4:
        return 'Friday'
    elif d == 5:
        return 'Saturday'
    else:
        return 'Sunday'
    
def next_birthday(d1):
    """Determines the amount of time remaining until the next birthday, given a 
    birthday.
    d1: datetime
    Returns: deltatime"""
    d = datetime.today()
    #next birthday
    d2 = datetime(d.year, d1.month, d1.day)
    if d > d2:
        d2 = datetime(d.year+1, d1.month, d1.day)
    
    return d2-d1

def double_day(d1, d2):
    """Finds the double-day given two birthdays, d1 > d2.
    d1: birthdate of younger person
    d2: birthdate of older person
    Returns: datetime of double-day"""
    diff = d1 - d2
    return datetime.date(d1 + diff)


def main():
    print get_day()
    print next_birthday(datetime.today())
    print double_day(datetime.today(), datetime(2011,1,1))

if __name__ == '__main__':
    main()

