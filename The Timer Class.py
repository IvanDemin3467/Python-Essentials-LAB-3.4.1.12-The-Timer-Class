# This is the Python Essentials 2 LAB 3.4.1.12 The Timer Class

def int_to_str(hrs):
    # This function adds leading zeros when the value is less than 10
    if hrs < 10:
        return "0" + str(hrs)
    else:
        return str(hrs)


def time_to_str(hrs, mins , sec):
    # This function implicitly convert time into string of the following form: "hh:mm:ss"
    return(int_to_str(hrs) + ":" +
           int_to_str(mins) + ":" +
           int_to_str(sec))


class Timer:
    def __init__(self, hrs = 0, mins = 0, sec = 0):
        # This constructor initiates private properties of the object
        self.__hrs = hrs
        self.__mins = mins
        self.__sec = sec

    def __str__(self):
        # This method makes class printable
        return time_to_str(self.__hrs, self.__mins , self.__sec)

    def next_second(self):
        # This method adds the next second and handles the overflow
        if self.__sec != 59:
            self.__sec += 1
        else:
            self.__sec = 0
            if self.__mins != 59:
                self.__mins += 1
            else:
                self.__mins = 0
                if self.__hrs != 23:
                    self.__hrs += 1
                else:
                    self.__hrs = 0

    def prev_second(self):
        # This method substracts the second and handles the overflow
        if self.__sec != 0:
            self.__sec -= 1
        else:
            self.__sec = 59
            if self.__mins != 0:
                self.__mins -= 1
            else:
                self.__mins = 59
                if self.__hrs != 0:
                    self.__hrs -= 1
                else:
                    self.__hrs = 23

if __name__ == "__main__":
    # this is some test code
    # Expected output
    # 23:59:59
    # 00:00:00
    # 23:59:59
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)

