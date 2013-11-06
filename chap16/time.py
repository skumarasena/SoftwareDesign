


class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour,t.minute, t.second)

def is_after(t1, t2):
    t1_sec = t1.hour*3600 + t1.minute*60 + t1.second
    t2_sec = t2.hour*3600 + t2.minute*60 + t2.second
    return t1_sec > t2_sec

def main():
    t1 = Time()
    t1.hour = 11
    t1.minute = 59
    t1.second = 30
    print_time(t1)

    t2 = Time()
    t2.hour = 11
    t2.minute = 30
    t2.second = 59
    print_time(t2)

    print is_after(t1, t2)

if __name__ == '__main__':
    main()
